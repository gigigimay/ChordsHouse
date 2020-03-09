from utilities.ui import refreshSongList, setCurrentSong, setCurrentSongListIndex
from service import add_song, edit_song


def onAccept(window):
    ui = window.ui
    mainUi = window.mainWindow.ui

    def handleChange():
        title = ui.titleInput.text()
        artist = ui.artistInput.text()
        lyrics = ui.lyricsInput.toPlainText()
        if title and lyrics:
            if ui.mode == 'add':
                id = add_song(title=title, artist=artist, lyrics=lyrics)
                refreshSongList(mainUi)

                # select new song on create
                newSong = list(filter(lambda song: song['_id'] == id, mainUi.allSongs))[0]
                newIndex = mainUi.allSongs.index(newSong)
                setCurrentSong(mainUi, newSong)
                setCurrentSongListIndex(mainUi, newIndex)

            elif ui.mode == 'edit':
                currentSongId = ui.currentSong['_id']
                edit_song(currentSongId, title=title, artist=artist, lyrics=lyrics)
                refreshSongList(mainUi)
            window.close()
        else:
            print('please fill all required data')
    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
