import re
from constants import ARTIST_PLACEHOLDER, CHORDS_PLACEHOLDER, DIVIDER
from utilities.transposer import transpose_line
import hashlib


def encode(str):
    return hashlib.md5(str.encode()).hexdigest()


def getSongLabel(song):
    return f'{song["title"]} - {song["artist"] or ARTIST_PLACEHOLDER}'


def getInitialChords(lyrics: str):
    lines = lyrics.splitlines()
    result = []
    for line in lines:
        l = f': \n> {line}' if line else ''
        result.append(l)
    return '\n'.join(result)


def getStripedText(lines, isStriped):
    result = []
    i = 0
    for line in lines:
        if line:
            div = f'<div class="{"odd" if (i % 2) and isStriped  else "even"}">{line}</div>'
            i += 1
        else:
            div = '<div> </div>'
            i = 0
        result.append(div)
    newText = ''.join(result)
    return newText


def wrapHtml(text, fontSize):
    style = f'''body {{
                white-space: pre-wrap;
                font-size:{fontSize}pt;
                font-family:'Overpass Mono';
                line-height: 80%;
            }}
            .even, .odd {{
                margin: {fontSize / 2}px 0;
            }}
            .odd {{
                background-color: #f3f3f3;
            }}
            .chords {{
                color: #333333;
                font-weight: bold;
            }}
            .invalid {{
                color: #c70431;
            }}'''
    return f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><style type="text/css">{style}</style></head>
            <body>{text}</body></html>'''

def getHtmlLyrics(text, fontSize, isStriped):
    lines = text.splitlines()
    result = getStripedText(lines, isStriped)
    return wrapHtml(result, fontSize)


def getHtmlChords(text, fontSize, transpose, isStriped):
    lines = text.splitlines()
    resultTemp = []
    tempC = []
    for line in lines:
        if line:
            if line[0] == '>':  # lyrics
                c = '<br>'.join(tempC)
                l = line[2:] or ' '
                resultTemp.append(f'<span class="chords">{c}</span><br>{l}')
                tempC = []
            elif line[0] == ':':  # chords
                try:
                    transposed = transpose_line(line[2:], transpose)
                    tempC.append(f'<span class="chords">{transposed}</span>')
                except:
                    tempC.append(f'<span class="chords invalid">{line[2:]}</span>')
            else:
                resultTemp.append(line)
        else:
            resultTemp.append('')
    result = getStripedText(resultTemp, isStriped)
    return wrapHtml(result, fontSize)


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
        for i, c in enumerate(chords):
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


def missingInt(nums):
    i = 1
    s = sorted(nums)
    for n in s:
        if n == i:
            i += 1
        else:
            break
    return i


def addCopySuffix(text: str, allTexts):
    text = re.sub(r'\s\s+', r' ', text)
    name = re.sub(r' - \d+$', '', text)
    nums = []
    for t in [text, *allTexts]:
        cleaned = re.sub(r'\s\s+', r' ', t)
        match = re.match(f'{name}.*', cleaned)
        num = re.findall(r'(?<= - )\d+$', cleaned)
        if match and num:
            nums.append(int(num[0]))
    newNum = missingInt(nums)
    return f'{name} - {newNum}'


def getSongTextFileBody(song):
    title = song['title']
    artist = song['artist'] or ARTIST_PLACEHOLDER
    lyrics = song['lyrics']
    return f'Title: {title}\nArtist: {artist}\n{DIVIDER}\n{lyrics}'


def getChordsTextFileBody(song, chords):
    title = song['title']
    artist = song['artist'] or ARTIST_PLACEHOLDER
    name = chords['title'] or CHORDS_PLACEHOLDER
    lyrics = chords['body']
    return f'Title: {title}\nArtist: {artist}\nChordsName: {name}\n{DIVIDER}\n{lyrics}'


def getValueFromKey(key, text):
    data = text.split(': ')
    if data[0] == key:
        return data[1]


def extractLyricsFromText(text: str):
    lines = text.splitlines()
    title = ''
    artist = ''
    if len(lines) >= 4 and lines[2] == DIVIDER:
        title = getValueFromKey('Title', lines.pop(0))
        artist = getValueFromKey('Artist', lines.pop(0))
        lines.pop(0)
    lyrics = '\n'.join(lines)
    return (title, artist, lyrics)


def extractChordsFromText(text: str):
    lines = text.splitlines()
    title = ''
    artist = ''
    name = ''
    if len(lines) >= 5 and lines[3] == DIVIDER:
        title = getValueFromKey('Title', lines.pop(0))
        artist = getValueFromKey('Artist', lines.pop(0))
        name = getValueFromKey('ChordsName', lines.pop(0))
        lines.pop(0)
    body = '\n'.join(lines)
    return (title, artist, name, body)
