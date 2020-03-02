import sys
import setupUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from UI.mainWindow import Ui_MainWindow
from UI.lyricsWindow import Ui_LyricsWindow
from UI.chordsWindow import Ui_ChordsWindow
from UI.confirmDialog import Ui_confirmDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.lyricsWindow = LyricsWindow(mainWindow=self)
        self.chordsWindow = ChordsWindow(mainWindow=self)
        self.confirmDialog = ConfirmDialog(mainWindow=self)
        setupUi.mainWindow(self)


class LyricsWindow(QWidget):
    def __init__(self, mainWindow=None):
        super(LyricsWindow, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_LyricsWindow()
        self.ui.setupUi(self)
        setupUi.lyricsWindow(self)


class ChordsWindow(QWidget):
    def __init__(self, mainWindow=None):
        super(ChordsWindow, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_ChordsWindow()
        self.ui.setupUi(self)
        setupUi.lyricsWindow(self)


class ConfirmDialog(QWidget):
    def __init__(self, mainWindow=None):
        super(ConfirmDialog, self).__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_confirmDialog()
        self.ui.setupUi(self)
        setupUi.confirmDialog(self)


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
