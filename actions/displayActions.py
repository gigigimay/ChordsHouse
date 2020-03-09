import constants as const
from utilities.ui import renderSongDetail, renderChordsBrowser
from UI.mainWindow import Ui_MainWindow


def onActionFontSize(ui, value):
    def handleChange():
        size = ui.lyricsFontSize + value
        if const.MAX_FONT_SIZE > size > const.MIN_FONT_SIZE:
            ui.lyricsFontSize = size
            renderSongDetail(ui)
            renderChordsBrowser(ui)

    return handleChange


def onActionStripedText(ui: Ui_MainWindow):
    def handleChange(bool):
        ui.stripedText = bool
        renderSongDetail(ui)
        renderChordsBrowser(ui)

    return handleChange
