import re
import constants as const
from PyQt5 import QtWidgets
from service import get_songs_list


def wrapHtml(self, text):
    newText = re.sub(r'\\n', '<br/>', text)
    size = self.lyricsFontSize
    bodyStyle = f'''white-space: pre-wrap;
        font-family:'.AppleSystemUIFont';
        font-size:{size}pt;
        font-weight:400;
        font-style:normal;
        '''
    bodyStyle = '{' + bodyStyle + '}'
    return f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><meta name="qrichtext" content="1" /><style type="text/css">
        body {bodyStyle}
        </style></head><body>{newText}</body></html>'''


def updateSongDetail(self):
    song = self.currentSong
    self.songTitleLabel.setText(song['title'])
    self.songArtistLabel.setText(song['artist'])
    self.lyricsTextView.setHtml(wrapHtml(self, song['lyrics']))


def setCurrentSong(self, song):
    self.currentSong = song
    updateSongDetail(self)


def renderSongItems(self, songs):
    self.songList.clear()
    for i, song in enumerate(songs):
        item = QtWidgets.QListWidgetItem()
        item.setText(f"{song['title']} - {song['artist']}")
        item.setData(const.SONG_ITEM_DATA_INDEX, song)
        self.songList.addItem(item)


def setAllSongs(self, songs):
    self.allSongs = songs
    renderSongItems(self, self.allSongs)


def refreshSongList(self):
    ## refresh song list
    newAllSongs = get_songs_list()
    self.allSongs = newAllSongs
    renderSongItems(self, self.allSongs)

    ## refresh current song
    prevSongId = self.currentSong['_id']
    matches = list(filter(lambda song: song['_id'] == prevSongId, newAllSongs))
    # refresh the song detail
    newCurrentSong = matches[0] if matches else newAllSongs[0]
    setCurrentSong(self, newCurrentSong)
    # reselect the song in songList widget
    index = newAllSongs.index(newCurrentSong)
    self.songList.setCurrentRow(index)

    # TODO: clear search inputs OR do the search again
