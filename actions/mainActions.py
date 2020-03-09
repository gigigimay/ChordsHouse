import constants as const
from utilities.ui import renderSongItems, setCurrentSong, setCurrentChordsIndex, renderSongDetail, \
    refreshSongList, initLyricsWindow, initDeleteSongDialog, initChordsWindow, initDeleteChordsDialog, setToolBar, \
    renderChordsBrowser


# --------------------------------- ui actions ---------------------------------
def onSearch(ui):
    def handleChange(text):
        def matchText(song):
            ltext = text.lower()
            return ltext in song['title'].lower() or ltext in song['artist'].lower()

        ui.songList.clear()
        filtered = filter(matchText, ui.allSongs)
        renderSongItems(ui, filtered)

    return handleChange


def onSongChanged(ui):
    def handleChange(item):
        if item:
            song = item.data(const.SONG_ITEM_DATA_INDEX)
            songId = song['_id']
            if ui.currentSong['_id'] != songId:
                setCurrentSong(ui, song)

    return handleChange


def onChordChanged(ui):
    def handleChange(index):
        print(f'onChordChanged >> {index}')
        setCurrentChordsIndex(ui, index)

    return handleChange


def onSongTabChanged(ui):
    def handleChange(i: int):
        setToolBar(ui, i)

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


# --------------------------------- song CRUD ---------------------------------
def onActionAddSong(window):
    def handleChange():
        initLyricsWindow(window.lyricsWindow)
        window.lyricsWindow.show()

    return handleChange


def onActionEditSong(window):
    def handleChange():
        initLyricsWindow(window.lyricsWindow, song=window.ui.currentSong)
        window.lyricsWindow.show()

    return handleChange


def onActionDeleteSong(window):
    def handleChange():
        initDeleteSongDialog(window.confirmDialog)
        window.confirmDialog.show()

    return handleChange


# --------------------------------- chords CRUD ---------------------------------
def onActionAddChord(window):
    def handleChange():
        initChordsWindow(window.chordsWindow)
        window.chordsWindow.show()

    return handleChange


def onActionEditChords(window):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords)
        window.chordsWindow.show()

    return handleChange


def onActionDuplicateChords(window):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords, duplicate=True)
        window.chordsWindow.show()

    return handleChange


def onActionDeleteChords(window):
    def handleChange():
        initDeleteChordsDialog(window.confirmDialog)
        window.confirmDialog.show()

    return handleChange
