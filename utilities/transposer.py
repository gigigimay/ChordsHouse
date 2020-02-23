"""
Modified from https://github.com/davidparsson/transposer
by May.
"""

import re

key_list = [('A',), ('A#', 'Bb'), ('B',), ('C',), ('C#', 'Db'), ('D',),
            ('D#', 'Eb'), ('E',), ('F',), ('F#', 'Gb'), ('G',), ('G#', 'Ab')]

sharp_flat = ['#', 'b']
sharp_flat_preferences = {
    'A': '#',
    'A#': 'b',
    'Bb': 'b',
    'B': '#',
    'C': 'b',
    'C#': 'b',
    'Db': 'b',
    'D': '#',
    'D#': 'b',
    'Eb': 'b',
    'E': '#',
    'F': 'b',
    'F#': '#',
    'Gb': '#',
    'G': '#',
    'G#': 'b',
    'Ab': 'b',
}

key_regex = re.compile(r'[ABCDEFG][#b]?')


def get_index_from_key(source_key):
    """Gets the internal index of a key
    >>> get_index_from_key('Bb')
    1
    """
    for key_names in key_list:
        if source_key in key_names:
            return key_list.index(key_names)
    raise Exception("Invalid key: %s" % source_key)


def get_key_from_index(index, to_key):
    """Gets the key at the given internal index.
    Sharp or flat depends on the target key.
    >>> get_key_from_index(1, 'Eb')
    'Bb'
    """
    key_names = key_list[index % len(key_list)]
    if len(key_names) > 1:
        sharp_or_flat = sharp_flat.index(sharp_flat_preferences[to_key])  # get #,b index from the preferences
        return key_names[sharp_or_flat]  #
    return key_names[0]


def get_transponation_steps(source_key, target_key):
    """Gets the number of half tones to transpose
    >>> get_transponation_steps('D', 'C')
    -2
    """
    source_index = get_index_from_key(source_key)
    target_index = get_index_from_key(target_key)
    return target_index - source_index


def transpose(source_chord, direction, to_key_param=''):
    """Transposes a chord a number of half tones.
    Sharp or flat depends on target key.
    >>> transpose('C', 3, 'Bb')
    'Eb'
    """
    to_key = to_key_param or source_chord
    source_index = get_index_from_key(source_chord)
    return get_key_from_index(source_index + direction, to_key)


def recursive_line_transpose(source_line, source_chords, direction, to_key):
    if not source_chords or not source_line:
        return source_line
    source_chord = source_chords.pop(0)
    chord_index = source_line.find(source_chord)
    after_chord_index = chord_index + len(source_chord)

    transposed = transpose(source_chord, direction, to_key)
    rest = recursive_line_transpose(source_line[after_chord_index:], source_chords, direction, to_key)
    return source_line[:chord_index] + transposed + rest


def transpose_line(source_line, direction, to_key=''):
    """
    Different keys will be sharp or flat depending on target key.
    >>> transpose_line('| A | A# | Bb | C#m7/F# |', -2, 'D')
    '| G | G# | G# | Bm7/E |'

    It will use the more common key if sharp/flat, for example F# instead of Gb.
    >>> transpose_line('| Gb |', 0, 'Gb')
    '| F# |'
    """
    source_chords = key_regex.findall(source_line)
    return recursive_line_transpose(source_line, source_chords, direction, to_key)


def transpose_lines(lines, direction, to_key=''):
    result = ''
    for line in lines:
        result += transpose_line(line, direction, to_key)
    return result
