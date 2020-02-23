import re
from utilities.transposer import transpose_line


def parseLyrics(lyrics):
    lines = lyrics.splitlines()
    result = []
    for t in lines:
        chordspattern = r'\[.+?\]'
        chordspattern2 = r'(?<=\[).+?(?=\])'
        lyricsline = re.sub(chordspattern, '', t)
        chords = list(re.finditer(chordspattern2, t))

        chordsline = ''
        curr = 0
        used = 0
        for i,c in enumerate(chords):
            word = c.group()
            start, end = c.span()
            length = len(word)

            startpos = start - used - (i * 2) - 1

            pad = startpos - curr

            chordsline = chordsline + (' ' * pad)
            chordsline = chordsline + word

            # update variables
            used = used + length
            curr = startpos + length

        result.append([chordsline, lyricsline])
    return result


if __name__ == '__main__':
    ll = '''[G] She had a [D]face straight out of magazine [Em7]      [Cadd9]
[G] God only [D]knows but you'll never leave her[Em7]      [Cadd9]'''
    r = parseLyrics(ll)
    for chl, lrl in r:
        print(transpose_line(chl, 2))
        print(lrl)
