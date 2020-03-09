import sys
import setupUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from UI.mainWindow import Ui_MainWindow
from UI.lyricsWindow import Ui_LyricsWindow
from UI.chordsWindow import Ui_ChordsWindow
from UI.confirmDialog import Ui_confirmDialog
from UI.chordsHelpDialog import Ui_chordsHelpDialog
from UI.alertBox import Ui_alertBox


class MainWindow(QMainWindow):
    allSongs = []
    currentSong = None
    allCurrentChords = []
    currentChordsIndex = -1

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lyricsWindow = LyricsWindow(mainWindow=self)
        self.chordsWindow = ChordsWindow(mainWindow=self)
        self.confirmDialog = ConfirmDialog(mainWindow=self)
        setupUi.mainWindow(self)

    def showAlert(self, text, title='Alert!'):
        self.alertBox = AlertBox(text, title)
        self.alertBox.show()


class LyricsWindow(QDialog):
    def __init__(self, mainWindow=None):
        super(LyricsWindow, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_LyricsWindow()
        self.ui.setupUi(self)
        self.setModal(True)
        setupUi.lyricsWindow(self)


class ChordsWindow(QDialog):
    def __init__(self, mainWindow=None):
        super(ChordsWindow, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_ChordsWindow()
        self.ui.setupUi(self)
        self.setModal(True)
        self.helpWindow = ChordsHelpDialog()
        setupUi.chordsWindow(self)


class ConfirmDialog(QDialog):
    def __init__(self, mainWindow=None):
        super(ConfirmDialog, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_confirmDialog()
        self.ui.setupUi(self)
        self.setModal(True)
        setupUi.confirmDialog(self)


class ChordsHelpDialog(QDialog):
    def __init__(self):
        super(ChordsHelpDialog, self).__init__()
        self.ui = Ui_chordsHelpDialog()
        self.ui.setupUi(self)
        setupUi.chordsHelpDialog(self)


class AlertBox(QDialog):
    def __init__(self, text, title):
        super(AlertBox, self).__init__()
        self.ui = Ui_alertBox()
        self.ui.setupUi(self)
        self.ui.label.setText(text)
        self.setWindowTitle(title)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
