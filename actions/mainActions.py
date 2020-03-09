import constants as const
from utilities.ui import setCurrentSong, setCurrentChordsIndex, renderSongDetail, \
    refreshSongList, initLyricsWindow, initDeleteSongDialog, initChordsWindow, initDeleteChordsDialog, setToolBar, \
    renderChordsBrowser, searchSong
from main import MainWindow


# --------------------------------- ui actions ---------------------------------
def onSearch(ui):
    def handleChange(text):
        searchSong(ui, text)

    return handleChange


def onSortByChanged(ui):
    def handleChange(index):
        if index == 1:
            ui.sortBy = 'artist'
        else:
            ui.sortBy = 'title'
        refreshSongList(ui)

    return handleChange


def onSongChanged(ui):
    def handleChange(item):
        if item:
            song = item.data(const.SONG_ITEM_DATA_INDEX)
            songId = song['_id']
            if ui.currentSong['_id'] != songId:
                setCurrentSong(ui, song)
                ui.actionTransposeReset.trigger()

    return handleChange


def onChordChanged(ui):
    def handleChange(index):
        setCurrentChordsIndex(ui, index)

    return handleChange


def onSongTabChanged(ui):
    def handleChange(i: int):
        setToolBar(ui, i)

    return handleChange


def onFavOnlyClicked(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onFavOnlyClicked')

    return handleChange


def onFavButtonClicked(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onFavButtonClicked')

    return handleChange


def onActionFontSize(ui, value):
    def handleChange():
        size = ui.lyricsFontSize + value
        if const.MAX_FONT_SIZE > size > const.MIN_FONT_SIZE:
            ui.lyricsFontSize = size
            renderSongDetail(ui)
            renderChordsBrowser(ui)

    return handleChange


def onActionTranspose(ui, value):
    def handleChange():
        if value:
            ui.transpose += value
        else:
            ui.transpose = 0
        ui.actionTransposeReset.setIconText(str(ui.transpose))
        ui.actionTransposeReset.setDisabled(ui.transpose == 0)
        renderChordsBrowser(ui)

    return handleChange


def onActionRefresh(ui):
    def handleChange():
        refreshSongList(ui)

    return handleChange


def onActionStripedText(ui):
    def handleChange():
        print('onActionStripedText')

    return handleChange


def onActionChordsChart(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionChordsChart')

    return handleChange


def onActionLogin(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionLogin')

    return handleChange


def onActionLogout(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionLogout')

    return handleChange


def onActionRegister(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionRegister')

    return handleChange


def onActionProfile(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionProfile')

    return handleChange


def onActionClearFav(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionClearFav')

    return handleChange


def onActionExportSong(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionExportSong')

    return handleChange


def onActionExportChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        print('onActionExportChords')

    return handleChange


# --------------------------------- song CRUD ---------------------------------
def onActionAddSong(window: MainWindow):
    def handleChange():
        initLyricsWindow(window.lyricsWindow)
        window.lyricsWindow.show()

    return handleChange


def onActionEditSong(window: MainWindow):
    def handleChange():
        initLyricsWindow(window.lyricsWindow, song=window.ui.currentSong)
        window.lyricsWindow.show()

    return handleChange


def onActionDeleteSong(window: MainWindow):
    def handleChange():
        initDeleteSongDialog(window.confirmDialog)
        window.confirmDialog.show()

    return handleChange


# --------------------------------- chords CRUD ---------------------------------
def onActionAddChord(window: MainWindow):
    def handleChange():
        initChordsWindow(window.chordsWindow)
        window.chordsWindow.show()

    return handleChange


def onActionEditChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords)
        window.chordsWindow.show()

    return handleChange


def onActionDuplicateChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords, duplicate=True)
        window.chordsWindow.show()

    return handleChange


def onActionDeleteChords(window: MainWindow):
    def handleChange():
        initDeleteChordsDialog(window.confirmDialog)
        window.confirmDialog.show()

    return handleChange
