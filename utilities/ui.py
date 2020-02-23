import re
import constants as const
from PyQt5 import QtWidgets
from service import get_song_data


def wrapHtml(self, text):
    newText = re.sub(r'\\n', '<br/>', text)
    size = self.lyricsFontSize
    bodyStyle = f'''white-space: pre-wrap; font-family:'.AppleSystemUIFont'; font-size:{size}pt; font-weight:400; font-style:normal;'''
    bodyStyle = '{' + bodyStyle + '}'
    return f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><meta name="qrichtext" content="1" /><style type="text/css">
        body {bodyStyle}
        </style></head><body>{newText}</body></html>'''


def setCurrentSong(self, id):
    self.currentSong = get_song_data(id)
    updateSongDetail(self)


def updateSongDetail(self):
    song = self.currentSong
    self.songTitleLabel.setText(song['title'])
    self.songArtistLabel.setText(song['artist'])
    self.lyricsTextView.setHtml(wrapHtml(self, song['lyrics']))


def onSearch(self):
    def handleChange(text):
        def matchText(song):
            ltext = text.lower()
            return ltext in song['title'].lower() or ltext in song['artist'].lower()
        self.songList.clear()
        filtered = filter(matchText, self.allSongs)
        renderSongItems(self, filtered)
    return handleChange


def renderSongItems(self, songs):
    self.songList.clear()
    for i, song in enumerate(songs):
        item = QtWidgets.QListWidgetItem()
        item.setText(f"{song['title']} - {song['artist']}")
        item.setData(const.SONG_ITEM_DATA_INDEX, song['_id'])
        self.songList.addItem(item)


def onSongClicked(self):
    def handleChange(item):
        songid = item.data(const.SONG_ITEM_DATA_INDEX)
        if self.currentSong['_id'] != songid:
            setCurrentSong(self, songid)
    return handleChange


def onActionFontSize(self, value):
    def handleChange():
        newSize = self.lyricsFontSize + value
        if newSize < const.MAX_FONT_SIZE and newSize > const.MIN_FONT_SIZE:
            self.lyricsFontSize = newSize
            updateSongDetail(self)
    return handleChange