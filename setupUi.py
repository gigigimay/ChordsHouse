from utilities.ui import renderSongItems, setCurrentSong, setCurrentTab, setCurrentSongListIndex
from actions import mainActions, lyricsActions, chordsActions, confirmDialogActions
from service import get_songs_list
from main import MainWindow, ChordsWindow, LyricsWindow

def mainWindow(window: MainWindow):
    ui = window.ui
    allSongs = get_songs_list('title')
    initialSongIndex = 0

    # init values
    ui.allSongs = allSongs
    ui.lyricsFontSize = 13
    ui.transpose = 0
    ui.sortBy = 'title'
    ui.stripedText = True

    # init ui
    setCurrentTab(ui, 0)
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
    ui.favOnlyCheckbox.clicked.connect(mainActions.onFavOnlyClicked(window))
    ui.favButton.clicked.connect(mainActions.onFavButtonClicked(window))

    # song actions
    ui.actionNewSong.triggered.connect(mainActions.onActionAddSong(window))
    ui.actionEditSong.triggered.connect(mainActions.onActionEditSong(window))
    ui.actionDeleteSong.triggered.connect(mainActions.onActionDeleteSong(window))
    ui.actionRefresh.triggered.connect(mainActions.onActionRefresh(ui))
    ui.actionExport_Song.triggered.connect(mainActions.onActionExportSong(window))

    # chord actions
    ui.actionAddChords.triggered.connect(mainActions.onActionAddChord(window))
    ui.actionEditChords.triggered.connect(mainActions.onActionEditChords(window))
    ui.actionDeleteChords.triggered.connect(mainActions.onActionDeleteChords(window))
    ui.actionDuplicateChords.triggered.connect(mainActions.onActionDuplicateChords(window))
    ui.actionTransposeUp.triggered.connect(mainActions.onActionTranspose(ui, 1))
    ui.actionTransposeDown.triggered.connect(mainActions.onActionTranspose(ui, -1))
    ui.actionTransposeReset.triggered.connect(mainActions.onActionTranspose(ui, 0))
    ui.actionChordsChart.triggered.connect(mainActions.onActionChordsChart(window))
    ui.actionExport_Chords.triggered.connect(mainActions.onActionExportChords(window))

    # display actions
    ui.actionFontBigger.triggered.connect(mainActions.onActionFontSize(ui, 3))
    ui.actionFontSmaller.triggered.connect(mainActions.onActionFontSize(ui, -3))
    ui.actionStriped_Text.triggered.connect(mainActions.onActionStripedText(ui))

    # profile actions
    ui.actionSign_In.triggered.connect(mainActions.onActionLogin(window))
    ui.actionSign_Out.triggered.connect(mainActions.onActionLogout(window))
    ui.actionSign_Up.triggered.connect(mainActions.onActionRegister(window))
    ui.actionClear_Favorites.triggered.connect(mainActions.onActionClearFav(window))
    ui.actionProfile.triggered.connect(mainActions.onActionProfile(window))


def lyricsWindow(window: LyricsWindow):
    ui = window.ui
    ui.buttonBox.accepted.connect(lyricsActions.onAccept(window))
    ui.buttonBox.rejected.connect(lyricsActions.onCancel(window))
    ui.importButton.clicked.connect(lyricsActions.onImport(window))


def chordsWindow(window: ChordsWindow):
    ui = window.ui
    ui.buttonBox.accepted.connect(chordsActions.onAccept(window))
    ui.buttonBox.rejected.connect(chordsActions.onCancel(window))
    ui.buttonBox.helpRequested.connect(chordsActions.onHelp(window))
    ui.importButton.clicked.connect(chordsActions.onImport(window))


def confirmDialog(window):
    ui = window.ui
    ui.deleteButton.clicked.connect(confirmDialogActions.onDelete(window))
    ui.cancelButton.clicked.connect(confirmDialogActions.onCancel(window))


def chordsHelpDialog(window):
    ui = window.ui
    # may change into own actions
    ui.pushButton.clicked.connect(confirmDialogActions.onCancel(window))