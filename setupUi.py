from utilities.ui import renderSongItems, setCurrentSong, setCurrentTab, setCurrentSongListIndex
from actions import mainActions, lyricsActions, chordsActions, confirmDialogActions
from service import get_songs_list


def mainWindow(window):
    ui = window.ui
    allSongs = get_songs_list('title')
    initialSongIndex = 0
    # init values
    ui.allSongs = allSongs
    ui.lyricsFontSize = 13
    ui.transpose = 0
    ui.sortBy = 'title'

    # init ui
    setCurrentTab(ui, 1)
    renderSongItems(ui, ui.allSongs)
    setCurrentSong(ui, allSongs[initialSongIndex])
    setCurrentSongListIndex(ui, initialSongIndex)
    ui.actionTransposeReset.setDisabled(ui.transpose == 0)

    # signal handling
    ui.searchInput.textChanged.connect(mainActions.onSearch(ui))
    ui.songList.currentItemChanged.connect(mainActions.onSongChanged(ui))
    ui.chordComboBox.currentIndexChanged.connect(mainActions.onChordChanged(ui))
    ui.songTabWidget.currentChanged.connect(mainActions.onSongTabChanged(ui))
    ui.sortByComboBox.currentIndexChanged.connect(mainActions.onSortByChanged(ui))
    ui.addChordButton.clicked.connect(mainActions.onActionAddChord(window))

    # action handling
    ui.actionNewSong.triggered.connect(mainActions.onActionAddSong(window))
    ui.actionEditSong.triggered.connect(mainActions.onActionEditSong(window))
    ui.actionDeleteSong.triggered.connect(mainActions.onActionDeleteSong(window))

    ui.actionAddChords.triggered.connect(mainActions.onActionAddChord(window))
    ui.actionEditChords.triggered.connect(mainActions.onActionEditChords(window))
    ui.actionDeleteChords.triggered.connect(mainActions.onActionDeleteChords(window))
    ui.actionDuplicateChords.triggered.connect(mainActions.onActionDuplicateChords(window))

    ui.actionFontBigger.triggered.connect(mainActions.onActionFontSize(ui, 3))
    ui.actionFontSmaller.triggered.connect(mainActions.onActionFontSize(ui, -3))
    ui.actionTransposeUp.triggered.connect(mainActions.onActionTranspose(ui, 1))
    ui.actionTransposeDown.triggered.connect(mainActions.onActionTranspose(ui, -1))
    ui.actionTransposeReset.triggered.connect(mainActions.onActionTranspose(ui, 0))
    ui.actionRefresh.triggered.connect(mainActions.onActionRefresh(ui))


def lyricsWindow(window):
    ui = window.ui
    ui.buttonBox.accepted.connect(lyricsActions.onAccept(window))
    ui.buttonBox.rejected.connect(lyricsActions.onCancel(window))


def chordsWindow(window):
    ui = window.ui
    ui.buttonBox.accepted.connect(chordsActions.onAccept(window))
    ui.buttonBox.rejected.connect(chordsActions.onCancel(window))
    ui.buttonBox.helpRequested.connect(chordsActions.onHelp(window))


def confirmDialog(window):
    ui = window.ui
    ui.deleteButton.clicked.connect(confirmDialogActions.onDelete(window))
    ui.cancelButton.clicked.connect(confirmDialogActions.onCancel(window))


def chordsHelpDialog(window):
    ui = window.ui
    # may change into own actions
    ui.pushButton.clicked.connect(confirmDialogActions.onCancel(window))