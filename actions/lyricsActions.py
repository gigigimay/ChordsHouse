from utilities.ui import refreshSongList, setCurrentSong, setCurrentSongListIndex
from service import add_song, edit_song


def onAccept(window):
    ui = window.ui
    mainWindow = window.mainWindow
    mainUi = mainWindow.ui

    def handleChange():
        title = ui.titleInput.text()
        artist = ui.artistInput.text()
        lyrics = ui.lyricsInput.toPlainText()
        if title and lyrics:
            if ui.mode == 'add':
                id = add_song(title=title, artist=artist, lyrics=lyrics)
                refreshSongList(mainUi)

                # select new song on create
                match = list(filter(lambda song: song['_id'] == id, mainUi.allSongs))
                if match:
                    newSong = match[0]
                    newIndex = mainUi.allSongs.index(newSong)
                    setCurrentSong(mainUi, newSong)
                    setCurrentSongListIndex(mainUi, newIndex)

            elif ui.mode == 'edit':
                currentSongId = ui.currentSong['_id']
                edit_song(currentSongId, title=title, artist=artist, lyrics=lyrics)
                refreshSongList(mainUi)
            window.close()
        elif not title:
            mainWindow.showAlert('Please fill in song title!')
            ui.titleInput.setFocus()
        elif not lyrics:
            mainWindow.showAlert('Please fill in song lyrics!')
            ui.lyricsInput.setFocus()
    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
