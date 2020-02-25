from utilities.ui import renderSongItems, setCurrentSong
from utilities.actions import onSearch, onSongChanged, onActionFontSize, onActionAddSong, onAddSongAccept, onActionRefresh
from service import get_songs_list

def mainWindow(self):
    # init values
    allSongs = get_songs_list()
    self.allSongs = allSongs
    self.lyricsFontSize = 14

    # init ui
    setCurrentSong(self, allSongs[0])
    renderSongItems(self, self.allSongs)

    # signal handling
    self.searchInput.textChanged.connect(onSearch(self))
    self.songList.currentItemChanged.connect(onSongChanged(self))
    self.actionFontBigger.triggered.connect(onActionFontSize(self, 3))
    self.actionFontSmaller.triggered.connect(onActionFontSize(self, -3))
    self.actionNewSong.triggered.connect(onActionAddSong(self))
    self.actionRefresh.triggered.connect(onActionRefresh(self))


def addSongWindow(self):
    self.buttonBox.accepted.connect(onAddSongAccept(self))
