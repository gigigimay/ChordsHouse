from utilities.ui import refreshSongList
from utilities.initWindow import initLyricsWindow, initDeleteSongDialog
from main import MainWindow
from utilities.utils import writeFile, getSaveFileName
from utilities.text import getSongLabel, getSongTextFileBody


def onActionRefresh(ui):
    def handleChange():
        refreshSongList(ui)

    return handleChange


def onActionExportSong(window: MainWindow):
    ui = window.ui

    def handleChange():
        song = ui.currentSong
        fileName = getSaveFileName(window, 'Export lyrics as', getSongLabel(song))
        if fileName[0]:
            body = getSongTextFileBody(song)
            writeFile(fileName[0], body)

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
