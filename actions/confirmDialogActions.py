from service import delete_song
import utilities


def onDelete(window):
    ui = window.ui

    def handleChange():
        if ui.mode == 'song':
            currentSongId = window.mainWindow.ui.currentSong['_id']
            delete_song(currentSongId)
        utilities.ui.refreshSongList(window.mainWindow.ui)
        window.close()
    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
