import constants as const
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from service import get_songs_list, get_song_chords_list, set_fav
from utilities.utils import getCurrentChordsData, setActionsDisabled, setWidgetsVisible, setActionsVisible
from utilities.text import getSongLabel, getHtmlLyrics, getHtmlChords
from constants import ARTIST_PLACEHOLDER, CHORDS_PLACEHOLDER


def setCurrentUser(ui, user):
    ui.userData = user
    if user:
        ui.actionSign_Out.setText(f'Sign Out ({user["username"]})')
    else:
        ui.favOnlyCheckbox.setChecked(False)
        ui.favButton.setText('+ Fav')
    refreshAccountActions(ui)
    renderFavButton(ui)


def toggleSongFav(ui):
    favSongs: list = ui.userData['favSongs']
    songId = ui.currentSong['_id']
    newFav = favSongs.copy()
    if songId in newFav:
        newFav.remove(songId)
    else:
        newFav.append(songId)
    setSongFav(ui, newFav)


def setSongFav(ui, newFav):
    user = ui.userData
    ui.userData['favSongs'] = newFav
    set_fav(user, newFav)
    renderFavButton(ui)
    ui.favButton.repaint()
    if ui.favOnlyCheckbox.isChecked():
        search = ui.searchInput.text()
        searchSong(ui, search)


def searchSong(ui, text):
    isFavOnly = ui.favOnlyCheckbox.isChecked()

    def match(song):
        if isFavOnly and song['_id'] not in ui.userData['favSongs']:
            return False
        lowerText = text.lower()
        return lowerText in song['title'].lower() or lowerText in song['artist'].lower()

    count = ui.songList.count()
    for i in range(count):
        item: QListWidgetItem = ui.songList.item(i)
        song = item.data(const.SONG_ITEM_DATA_INDEX)
        item.setHidden(not match(song))


def setToolBar(ui, i):
    # must hide old toolbar first, to prevent flashy ui
    if i:
        ui.lyricsToolBar.setVisible(False)
        ui.chordsToolBar.setVisible(True)
    else:
        ui.chordsToolBar.setVisible(False)
        ui.lyricsToolBar.setVisible(True)


def setCurrentTab(ui, index):
    ui.songTabWidget.setCurrentIndex(index)
    setToolBar(ui, index)


def setCurrentSong(ui, song):
    # song
    ui.currentSong = song
    renderSongDetail(ui)
    renderFavButton(ui)

    # chords
    chords = get_song_chords_list(song['_id'])
    index = 0 if chords else -1
    ui.allCurrentSongChords = chords
    ui.currentChordsIndex = index
    updateChordsUi(ui)


def setCurrentSongListIndex(ui, index):
    ui.songList.setCurrentRow(index)


def renderSongItems(ui, songs):
    ui.songList.clear()
    for song in songs:
        item = QtWidgets.QListWidgetItem()
        item.setText(getSongLabel(song))
        item.setData(const.SONG_ITEM_DATA_INDEX, song)
        ui.songList.addItem(item)


def refreshSongList(ui):
    # refresh song list
    newAllSongs = get_songs_list(ui.sortBy)
    ui.allSongs = newAllSongs
    renderSongItems(ui, ui.allSongs)

    # refresh current song
    currentSongId = ui.currentSong['_id']
    matches = list(filter(lambda song: song['_id'] == currentSongId, newAllSongs))
    # refresh the song detail
    newCurrentSong = matches[0] if matches else newAllSongs[0]
    setCurrentSong(ui, newCurrentSong)
    # reselect the song in songList widget
    index = newAllSongs.index(newCurrentSong)
    ui.songList.setCurrentRow(index)

    search = ui.searchInput.text()
    searchSong(ui, search)


def setCurrentChordsIndex(ui, index):
    ui.currentChordsIndex = index
    renderChordsBrowser(ui)


def renderSongDetail(ui):
    song = ui.currentSong
    lyrics = getHtmlLyrics(song['lyrics'], ui.lyricsFontSize, ui.stripedText)
    ui.songTitleLabel.setText(song['title'])
    ui.songArtistLabel.setText(song['artist'] or ARTIST_PLACEHOLDER)
    ui.lyricsTextView.setHtml(lyrics)


def renderFavButton(ui):
    print('renderFavButton')
    user = ui.userData
    buttonText = '+ Fav'
    prevText = ui.favButton.text()
    if user:
        favSongs: list = user['favSongs']
        if ui.currentSong['_id'] in favSongs:
            buttonText = '- Fav'
    if buttonText != prevText:
        ui.favButton.setText(buttonText)


def refreshAccountActions(ui):
    haveUser = bool(ui.userData)
    dontHaveUserActions = [ui.actionSign_In, ui.actionSign_Up]
    setActionsDisabled(not haveUser, [
        ui.actionChangePassword,
        ui.actionClear_Favorites,
        ui.actionSign_Out
    ])
    setActionsDisabled(haveUser, dontHaveUserActions)
    setActionsVisible(haveUser, [ui.actionSign_Out])
    setActionsVisible(not haveUser, dontHaveUserActions)


# ---------------------------- chords ----------------------------
def refreshChordsData(ui, newIndex=None):
    song = ui.currentSong
    chords = get_song_chords_list(song['_id'])
    index = 0 if chords else -1
    ui.allCurrentSongChords = chords
    ui.currentChordsIndex = newIndex or index
    updateChordsUi(ui)


def updateChordsUi(ui):
    index = ui.currentChordsIndex
    chords = ui.allCurrentSongChords
    setChordsDisabled(ui, not chords)
    dropdown: QtWidgets.QComboBox = ui.chordComboBox

    # these lines are causing over rerendering/
    dropdown.clear()
    if chords:
        for c in chords:
            dropdown.addItem(c['title'] or CHORDS_PLACEHOLDER)
        dropdown.setCurrentIndex(index)
        renderChordsBrowser(ui)


def setChordsDisabled(ui, disabled):
    actions = [
        ui.actionEditChords,
        ui.actionDeleteChords,
        ui.actionChordsChart,
        ui.actionTransposeUp,
        ui.actionTransposeDown,
        ui.actionTransposeReset,
        ui.actionDuplicateChords,
    ]
    haveChordsWidgets = [ui.chordComboBox, ui.chordsTextView]
    dontHaveChordsWidgets = [ui.addChordButton]
    setActionsDisabled(disabled, actions)
    setWidgetsVisible(not disabled, haveChordsWidgets)
    setWidgetsVisible(disabled, dontHaveChordsWidgets)


def renderChordsBrowser(ui):
    chords = getCurrentChordsData(ui)
    if chords:
        body = getHtmlChords(chords['body'], ui.lyricsFontSize, ui.transpose, ui.stripedText)
        ui.chordsTextView.setHtml(body)
