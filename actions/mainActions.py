import constants as const
from utilities.ui import renderSongItems, setCurrentSong, updateSongDetail, refreshSongList, initLyricsWindow, initDeleteDialog


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
        if i:
            ui.lyricsToolBar.hide()
            ui.chordsToolBar.show()
        else:
            ui.chordsToolBar.hide()
            ui.lyricsToolBar.show()
    return handleChange


def onActionFontSize(ui, value):
    def handleChange():
        size = ui.lyricsFontSize + value
        if const.MAX_FONT_SIZE > size > const.MIN_FONT_SIZE:
            ui.lyricsFontSize = size
            updateSongDetail(ui)
    return handleChange


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
        initDeleteDialog(window.confirmDialog)
        window.confirmDialog.show()
    return handleChange


def onActionRefresh(ui):
    def handleChange():
        refreshSongList(ui)
    return handleChange
