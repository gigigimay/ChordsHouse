from utilities.ui import refreshSongList
from service import add_chords, edit_chords

def onAccept(window):
    ui = window.ui

    def handleChange():
        title = ui.chordsNameInput.text()
        body = ui.lyricsInput.toPlainText()
        currentSongId = ui.currentSong['_id']
        if body:
            if ui.mode == 'add':
                add_chords(title=title, body=body, songId=currentSongId)
            elif ui.mode == 'edit':
                currentChordsId = ui.currentChords['_id']
                edit_chords(currentChordsId, title=title, body=body)
            refreshSongList(window.mainWindow.ui)
            window.close()
        else:
            print('please fill all required data')

    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
