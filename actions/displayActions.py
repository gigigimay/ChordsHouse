import constants as const
from utilities.ui import renderSongDetail, renderChordsBrowser
from UI.mainWindow import Ui_MainWindow


def onActionFontSize(ui, value):
    def handleChange():
        size = ui.lyricsFontSize + value
        change = False
        if value == 0:
            ui.lyricsFontSize = 13
            change = True
        elif const.MAX_FONT_SIZE > size > const.MIN_FONT_SIZE:
            ui.lyricsFontSize = size
            change = True
        if change:
            renderSongDetail(ui)
            renderChordsBrowser(ui)

    return handleChange


def onActionStripedText(ui: Ui_MainWindow):
    def handleChange(bool):
        ui.stripedText = bool
        renderSongDetail(ui)
        renderChordsBrowser(ui)

    return handleChange
