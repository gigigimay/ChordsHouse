from utilities.ui import refreshSongList
from service import add_song, edit_song


def onAccept(window):
    ui = window.ui

    def handleChange():
        title = ui.titleInput.text()
        artist = ui.artistInput.text()
        lyrics = ui.lyricsInput.toPlainText()
        if title and lyrics:
            if ui.mode == 'add':
                add_song(title=title, artist=artist, lyrics=lyrics)
            elif ui.mode == 'edit':
                currentSongId = ui.currentSong['_id']
                edit_song(currentSongId, title=title, artist=artist, lyrics=lyrics)
            refreshSongList(window.mainWindow.ui)
            window.close()
        else:
            print('please fill all required data')
    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
