from utilities.ui import renderSongItems, setCurrentSong, setCurrentTab
from actions import mainActions, lyricsActions, chordsActions, confirmDialogActions
from service import get_songs_list


def mainWindow(window):
    ui = window.ui
    # init values
    allSongs = get_songs_list()
    ui.allSongs = allSongs
    ui.lyricsFontSize = 13

    # init ui
    setCurrentSong(ui, allSongs[0])
    renderSongItems(ui, ui.allSongs)
    setCurrentTab(ui, 1)


    # signal handling
    ui.searchInput.textChanged.connect(mainActions.onSearch(ui))
    ui.songList.currentItemChanged.connect(mainActions.onSongChanged(ui))
    ui.songTabWidget.currentChanged.connect(mainActions.onSongTabChanged(ui))

    # action handling
    ui.actionNewSong.triggered.connect(mainActions.onActionAddSong(window))
    ui.actionEditSong.triggered.connect(mainActions.onActionEditSong(window))
    ui.actionDeleteSong.triggered.connect(mainActions.onActionDeleteSong(window))
    ui.actionAddChords.triggered.connect(mainActions.onActionAddChord(window))
    ui.actionEditChords.triggered.connect(mainActions.onActionEditChords(window))
    ui.actionDeleteChords.triggered.connect(mainActions.onActionDeleteChords(window))
    ui.actionFontBigger.triggered.connect(mainActions.onActionFontSize(ui, 3))
    ui.actionFontSmaller.triggered.connect(mainActions.onActionFontSize(ui, -3))
    ui.actionRefresh.triggered.connect(mainActions.onActionRefresh(ui))


def lyricsWindow(window):
    ui = window.ui
    ui.buttonBox.accepted.connect(lyricsActions.onAccept(window))
    ui.buttonBox.rejected.connect(lyricsActions.onCancel(window))


def chordsWindow(window):
    ui = window.ui
    ui.buttonBox.accepted.connect(chordsActions.onAccept(window))
    ui.buttonBox.rejected.connect(chordsActions.onCancel(window))


def confirmDialog(window):
    ui = window.ui
    ui.buttonBox.rejected.connect(confirmDialogActions.onCancel(window))
    ui.buttonBox.accepted.connect(confirmDialogActions.onDelete(window))
