from utilities.ui import renderSongItems, onSearch, onSongClicked, updateSongDetail, setCurrentSong
from service import get_songs_list, get_song_data

def setupUi(self):
    # initiate ui
    allSongs = get_songs_list()
    self.allSongs = allSongs
    setCurrentSong(self, allSongs[0]['_id'])
    renderSongItems(self, self.allSongs)

    # event handling
    self.searchInput.textChanged.connect(onSearch(self))
    self.songList.itemClicked.connect(onSongClicked(self))