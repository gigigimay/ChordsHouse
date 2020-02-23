from PyQt5 import QtWidgets
from utilities.utils import wrapHtml
from service import get_song_data
import constants


def setCurrentSong(self, id):
    self.currentSong = get_song_data(id)
    updateSongDetail(self)


def updateSongDetail(self):
    song = self.currentSong
    self.songTitleLabel.setText(song['title'])
    self.songArtistLabel.setText(song['artist'])
    self.lyricsTextView.setHtml(wrapHtml(song['lyrics']))


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
        item.setData(constants.SONG_ITEM_DATA_INDEX, song['_id'])
        self.songList.addItem(item)


def onSongClicked(self):
    def handleChange(item):
        songid = item.data(constants.SONG_ITEM_DATA_INDEX)
        if self.currentSong['_id'] != songid:
            setCurrentSong(self, songid)
    return handleChange