from utilities.ui import renderSongItems, setCurrentSong, setCurrentTab, setCurrentSongListIndex, refreshAccountActions
from actions import mainActions, lyricsDialogActions, chordsDialogActions, confirmDialogActions, chordsActions, \
    commonActions, displayActions, accountActions, songActions
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
    ui.userData = None

    # init ui
    setCurrentTab(ui, 0)
    renderSongItems(ui, ui.allSongs)
    setCurrentSong(ui, allSongs[initialSongIndex])
    setCurrentSongListIndex(ui, initialSongIndex)
    refreshAccountActions(ui)
    ui.actionTransposeReset.setDisabled(ui.transpose == 0)

    # signal handling
    ui.searchInput.textChanged.connect(mainActions.onSearch(ui))
    ui.songList.currentItemChanged.connect(mainActions.onSongChanged(ui))
    ui.chordComboBox.currentIndexChanged.connect(mainActions.onChordChanged(ui))
    ui.songTabWidget.currentChanged.connect(mainActions.onSongTabChanged(ui))
    ui.sortByComboBox.currentIndexChanged.connect(mainActions.onSortByChanged(ui))
    ui.favOnlyCheckbox.clicked.connect(mainActions.onFavOnlyClicked(window))
    ui.favButton.clicked.connect(mainActions.onFavButtonClicked(window))
    ui.addChordButton.clicked.connect(chordsActions.onActionAddChord(window))

    # song actions
    ui.actionNewSong.triggered.connect(songActions.onActionAddSong(window))
    ui.actionEditSong.triggered.connect(songActions.onActionEditSong(window))
    ui.actionDeleteSong.triggered.connect(songActions.onActionDeleteSong(window))
    ui.actionRefresh.triggered.connect(songActions.onActionRefresh(ui))
    ui.actionExport_Song.triggered.connect(songActions.onActionExportSong(window))

    # chord actions
    ui.actionAddChords.triggered.connect(chordsActions.onActionAddChord(window))
    ui.actionEditChords.triggered.connect(chordsActions.onActionEditChords(window))
    ui.actionDeleteChords.triggered.connect(chordsActions.onActionDeleteChords(window))
    ui.actionDuplicateChords.triggered.connect(chordsActions.onActionDuplicateChords(window))
    ui.actionTransposeUp.triggered.connect(chordsActions.onActionTranspose(ui, 1))
    ui.actionTransposeDown.triggered.connect(chordsActions.onActionTranspose(ui, -1))
    ui.actionTransposeReset.triggered.connect(chordsActions.onActionTranspose(ui, 0))
    ui.actionChordsChart.triggered.connect(chordsActions.onActionChordsChart(window))
    ui.actionExport_Chords.triggered.connect(chordsActions.onActionExportChords(window))

    # display actions
    ui.actionFontBigger.triggered.connect(displayActions.onActionFontSize(ui, 3))
    ui.actionFontSmaller.triggered.connect(displayActions.onActionFontSize(ui, -3))
    ui.actionStriped_Text.triggered.connect(displayActions.onActionStripedText(ui))

    # profile actions
    ui.actionSign_In.triggered.connect(accountActions.onActionLogin(window))
    ui.actionSign_Out.triggered.connect(accountActions.onActionLogout(window))
    ui.actionSign_Up.triggered.connect(accountActions.onActionRegister(window))
    ui.actionClear_Favorites.triggered.connect(accountActions.onActionClearFav(window))
    ui.actionProfile.triggered.connect(accountActions.onActionProfile(window))


def lyricsWindow(window: LyricsWindow):
    ui = window.ui
    ui.buttonBox.accepted.connect(lyricsDialogActions.onAccept(window))
    ui.buttonBox.rejected.connect(commonActions.onCancel(window))
    ui.importButton.clicked.connect(lyricsDialogActions.onImport(window))


def chordsWindow(window: ChordsWindow):
    ui = window.ui
    ui.buttonBox.accepted.connect(chordsDialogActions.onAccept(window))
    ui.buttonBox.rejected.connect(commonActions.onCancel(window))
    ui.buttonBox.helpRequested.connect(chordsDialogActions.onHelp(window))
    ui.importButton.clicked.connect(chordsDialogActions.onImport(window))


def confirmDialog(window):
    ui = window.ui
    ui.deleteButton.clicked.connect(confirmDialogActions.onDelete(window))
    ui.cancelButton.clicked.connect(commonActions.onCancel(window))


def chordsHelpDialog(window):
    ui = window.ui
    ui.pushButton.clicked.connect(commonActions.onCancel(window))
