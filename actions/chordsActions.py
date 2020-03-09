from utilities.ui import refreshSongList, refreshChordsData
from service import add_chords, edit_chords

def onAccept(window):
    ui = window.ui
    mainUi = window.mainWindow.ui

    def handleChange():
        title = ui.chordsNameInput.text()
        body = ui.lyricsInput.toPlainText()
        currentSongId = ui.currentSong['_id']
        if body:
            if ui.mode == 'add':
                newIndex = len(mainUi.allCurrentSongChords)
                add_chords(title=title, body=body, songId=currentSongId)
                refreshSongList(mainUi)
                refreshChordsData(mainUi, newIndex=newIndex)
            elif ui.mode == 'edit':
                currentChordsId = ui.currentChords['_id']
                currentChordsIndex = mainUi.currentChordsIndex
                edit_chords(currentChordsId, title=title, body=body)
                refreshChordsData(mainUi, newIndex=currentChordsIndex)
            window.close()
        else:
            print('please fill all required data')

    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange


def onHelp(window):
    def handleChange():
        window.helpWindow.show()
    return handleChange