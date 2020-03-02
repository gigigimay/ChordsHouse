import constants as const
from utilities.ui import renderSongItems, setCurrentSong, updateSongDetail, refreshSongList, initLyricsWindow, initDeleteSongDialog, initChordsWindow, initDeleteChordsDialog, setToolBar


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
            if ui.currentSong['_id'] != song['_id']:
                setCurrentSong(ui, song)
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
            updateSongDetail(ui)
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
    def handleChange():
        initChordsWindow(window.chordsWindow, song=window.ui.currentChords)
        window.chordsWindow.show()
    return handleChange


def onActionDeleteChords(window):
    def handleChange():
        initDeleteChordsDialog(window.confirmDialog)
        window.confirmDialog.show()
    return handleChange


def onActionRefresh(ui):
    def handleChange():
        refreshSongList(ui)
    return handleChange
