from service import delete_song, delete_chords
import utilities


def onDelete(window):
    ui = window.ui
    mainUi = window.mainWindow.ui

    def handleChange():
        if ui.mode == 'song':
            currentSongId = window.mainWindow.ui.currentSong['_id']
            delete_song(currentSongId)
            utilities.ui.setCurrentTab(mainUi, 0)
        if ui.mode == 'chords':
            currentChordsId = utilities.ui.getCurrentChordsData(window.mainWindow.ui)['_id']
            delete_chords(currentChordsId)
            utilities.ui.setCurrentTab(mainUi, 1)
        utilities.ui.refreshSongList(window.mainWindow.ui)
        window.close()

    return handleChange
