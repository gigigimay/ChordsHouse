import constants as const
from utilities.ui import renderSongItems, setCurrentSong, updateSongDetail, refreshSongList
from PyQt5 import QtWidgets
from UI.addSongWindow import Ui_AddSong


def onSearch(self):
    def handleChange(text):
        def matchText(song):
            ltext = text.lower()
            return ltext in song['title'].lower() or ltext in song['artist'].lower()
        self.songList.clear()
        filtered = filter(matchText, self.allSongs)
        renderSongItems(self, filtered)
    return handleChange


def onSongChanged(self):
    def handleChange(item):
        if item:
            song = item.data(const.SONG_ITEM_DATA_INDEX)
            if self.currentSong['_id'] != song['_id']:
                setCurrentSong(self, song)
    return handleChange


def onActionFontSize(self, value):
    def handleChange():
        newSize = self.lyricsFontSize + value
        if newSize < const.MAX_FONT_SIZE and newSize > const.MIN_FONT_SIZE:
            self.lyricsFontSize = newSize
            updateSongDetail(self)
    return handleChange


def onActionAddSong(self):
    def handleChange():
        print('open addsong dialog')
        # add song dialog
        self.AddSongWindow = QtWidgets.QWidget()
        self.uiAddSong = Ui_AddSong()
        self.uiAddSong.setupUi(self.AddSongWindow)
        self.AddSongWindow.show()
    return handleChange


def onAddSongAccept(self):
    def handleChange():
        print('addSong')
    return handleChange


def onActionRefresh(self):
    def handleChange():
        refreshSongList(self)
    return handleChange