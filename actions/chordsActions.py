from utilities.ui import renderChordsBrowser
from utilities.initWindow import initChordsWindow, initDeleteChordsDialog
from utilities.utils import writeFile, getCurrentChordsData, getSaveFileName
from utilities.text import getSongLabel, getChordsTextFileBody
from main import MainWindow
from constants import CHORDS_PLACEHOLDER
import webbrowser


def onActionChordsChart():
    def handleChange():
        webbrowser.open('https://cdn.lessons.com/assets/images/courses/guitar/guitar-chords-chart.jpg')

    return handleChange


def onActionTranspose(ui, value):
    def handleChange():
        if value:
            ui.transpose += value
        else:
            ui.transpose = 0
        ui.actionTransposeReset.setIconText(str(ui.transpose))
        ui.actionTransposeReset.setDisabled(ui.transpose == 0)
        renderChordsBrowser(ui)

    return handleChange


def onActionExportChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        song = ui.currentSong
        chords = getCurrentChordsData(ui)
        chordsTitle = chords['title'] or CHORDS_PLACEHOLDER
        fileName = getSaveFileName(window, 'Export lyrics as', f'{getSongLabel(song)} - {chordsTitle}')
        if fileName[0]:
            body = getChordsTextFileBody(song, chords)
            writeFile(fileName[0], body)

    return handleChange


# --------------------------------- chords CRUD ---------------------------------
def onActionAddChord(window: MainWindow):
    def handleChange():
        initChordsWindow(window.chordsWindow)
        window.chordsWindow.show()

    return handleChange


def onActionEditChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords)
        window.chordsWindow.show()

    return handleChange


def onActionDuplicateChords(window: MainWindow):
    ui = window.ui

    def handleChange():
        chords = ui.allCurrentSongChords[ui.currentChordsIndex]
        initChordsWindow(window.chordsWindow, chords=chords, duplicate=True)
        window.chordsWindow.show()

    return handleChange


def onActionDeleteChords(window: MainWindow):
    def handleChange():
        initDeleteChordsDialog(window.confirmDialog)
        window.confirmDialog.show()

    return handleChange
