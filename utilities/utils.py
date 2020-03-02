import re
from bson.objectid import ObjectId
from constants import ARTIST_PLACEHOLDER


def createObjId(id: str):
    return ObjectId(id)


def dump(obj):
  for attr in dir(obj):
      print("obj.%s = %r" % (attr, getattr(obj, attr)))


def getSongLabel(song):
    return f'{song["title"]} - {song["artist"] or ARTIST_PLACEHOLDER}'


def getInitialChords(lyrics: str):
    lines = lyrics.splitlines()
    return '\n'.join([f'\n{line}' for line in lines])


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
