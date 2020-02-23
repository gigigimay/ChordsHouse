from utilities.ui import renderSongItems, onSearch, onSongClicked, onActionFontSize, setCurrentSong
from service import get_songs_list, get_song_data

def setupUi(self):
    # init values
    allSongs = get_songs_list()
    self.allSongs = allSongs
    self.lyricsFontSize = 14

    # init ui
    setCurrentSong(self, allSongs[0]['_id'])
    renderSongItems(self, self.allSongs)

    # event handling
    self.searchInput.textChanged.connect(onSearch(self))
    self.songList.itemClicked.connect(onSongClicked(self))
    self.actionFontBigger.triggered.connect(onActionFontSize(self, 3))
    self.actionFontSmaller.triggered.connect(onActionFontSize(self, -3))