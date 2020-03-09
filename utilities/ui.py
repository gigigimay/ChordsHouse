import constants as const
from PyQt5 import QtWidgets
from service import get_songs_list, get_song_chords_list
from utilities.utils import getCurrentChordsData, setActionsDisabled, setWidgetsVisible
from utilities.text import getSongLabel, getInitialChords, getHtmlLyrics, addCopySuffix, getHtmlChords
from constants import ARTIST_PLACEHOLDER, CHORDS_PLACEHOLDER


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
    newAllSongs = get_songs_list()
    ui.allSongs = newAllSongs
    renderSongItems(ui, ui.allSongs)

    ### refresh current song
    currentSongId = ui.currentSong['_id']
    matches = list(filter(lambda song: song['_id'] == currentSongId, newAllSongs))
    # refresh the song detail
    newCurrentSong = matches[0] if matches else newAllSongs[0]
    setCurrentSong(ui, newCurrentSong)
    # reselect the song in songList widget
    index = newAllSongs.index(newCurrentSong)
    ui.songList.setCurrentRow(index)

    # TODO: clear search inputs OR do the search again


def setCurrentChordsIndex(ui, index):
    ui.currentChordsIndex = index
    renderChordsBrowser(ui)


def renderSongDetail(ui):
    song = ui.currentSong
    lyrics = getHtmlLyrics(song['lyrics'], ui.lyricsFontSize)
    ui.songTitleLabel.setText(song['title'])
    ui.songArtistLabel.setText(song['artist'] or ARTIST_PLACEHOLDER)
    ui.lyricsTextView.setHtml(lyrics)


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
        body = getHtmlChords(chords['body'], ui.lyricsFontSize, ui.transpose)
        ui.chordsTextView.setHtml(body)

# ---------------------------- ui init ----------------------------
def initLyricsWindow(window, song=None):
    ui = window.ui
    ui.titleInput.setFocus()
    ui.currentSong = song
    if not song:
        ui.mode = 'add'
        ui.titleInput.setText('')
        ui.artistInput.setText('')
        ui.lyricsInput.setPlainText('')
        window.setWindowTitle('New Song')
        ui.dialogTitleLabel.setText('New Song')
    else:
        ui.mode = 'edit'
        ui.titleInput.setText(song['title'])
        ui.artistInput.setText(song['artist'])
        ui.lyricsInput.setPlainText(song['lyrics'])
        window.setWindowTitle('Edit Song')
        ui.dialogTitleLabel.setText('Edit Song')


def initChordsWindow(window, chords=None, duplicate=False):
    ui = window.ui
    song = window.mainWindow.ui.currentSong

    ui.chordsNameInput.setFocus()
    ui.currentChords = chords
    ui.currentSong = song
    ui.songTitleLabel.setText(song['title'])
    ui.songArtistLabel.setText(song['artist'])
    if not chords:
        ui.mode = 'add'
        windowTitle = 'New Chords'
        chordsTitle = ''
        chordsBody = getInitialChords(song['lyrics'])
    elif duplicate:
        allChordsName = [c['title'] or CHORDS_PLACEHOLDER for c in window.mainWindow.ui.allCurrentSongChords]
        ui.mode = 'add'
        windowTitle = 'Duplicate Chords'
        chordsTitle = addCopySuffix(f"{chords['title'] or CHORDS_PLACEHOLDER}", allChordsName)
        chordsBody = chords['body']
    else:
        ui.mode = 'edit'
        windowTitle = 'Edit Chords'
        chordsTitle = chords['title']
        chordsBody = chords['body']
    ui.chordsNameInput.setText(chordsTitle)
    ui.lyricsInput.setPlainText(chordsBody)
    window.setWindowTitle(windowTitle)
    ui.dialogTitleLabel.setText(windowTitle)


def initDeleteSongDialog(window):
    ui = window.ui
    ui.mode = 'song'
    label = getSongLabel(window.mainWindow.ui.currentSong)
    ui.label.setText(f'Confirm Deletion?\n{label}')


def initDeleteChordsDialog(window):
    ui = window.ui
    ui.mode = 'chords'
    label = getSongLabel(window.mainWindow.ui.currentSong)
    currentChords = getCurrentChordsData(window.mainWindow.ui)
    chordName = currentChords['title'] or CHORDS_PLACEHOLDER
    ui.label.setText(f'Confirm Deletion?\n"{chordName}"\n{label}')
