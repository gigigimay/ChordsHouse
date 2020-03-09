from utilities.ui import refreshSongList, refreshChordsData, setCurrentTab
from utilities.utils import getOpenFileContent
from utilities.text import extractChordsFromText
from service import add_chords, edit_chords
from main import ChordsWindow

def onAccept(window):
    ui = window.ui
    mainWindow = window.mainWindow
    mainUi = mainWindow.ui

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
            setCurrentTab(mainUi, 1)
            window.close()
        else:
            mainWindow.showAlert('Chords cannot be empty!')
            ui.lyricsInput.setFocus()


    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange


def onHelp(window):
    def handleChange():
        window.helpWindow.show()
    return handleChange


def onImport(window: ChordsWindow):
    ui = window.ui

    def handleChange():
        result = getOpenFileContent(window, 'Import Song Lyrics')
        if result:
            (title, artist, name, body) = extractChordsFromText(result)
            ui.chordsNameInput.setText(name)
            ui.lyricsInput.setPlainText(body)

    return handleChange
