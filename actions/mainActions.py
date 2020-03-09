import constants as const
from utilities.ui import setCurrentSong, setCurrentChordsIndex, refreshSongList, setToolBar, searchSong
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

    def handleChange(value):
        print(f'onFavButtonClicked >> {value}')
        if not ui.userData:
            ui.favOnlyCheckbox.setChecked(False)
            ui.actionSign_In.trigger()

    return handleChange


def onFavButtonClicked(window: MainWindow):
    ui = window.ui

    def handleChange(value):
        print(f'onFavButtonClicked >> {value}')
        if not ui.userData:
            ui.actionSign_In.trigger()

    return handleChange
