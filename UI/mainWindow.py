# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(7)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayoutL = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayoutL.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutL.setObjectName("verticalLayoutL")
        self.labelSongs_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelSongs_2.setFont(font)
        self.labelSongs_2.setObjectName("labelSongs_2")
        self.verticalLayoutL.addWidget(self.labelSongs_2)
        self.songList = QtWidgets.QListWidget(self.layoutWidget)
        self.songList.setObjectName("songList")
        self.verticalLayoutL.addWidget(self.songList)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutL.addWidget(self.line)
        self.searchInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.verticalLayoutL.addWidget(self.searchInput)
        self.favOnlyCheckbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.favOnlyCheckbox.setObjectName("favOnlyCheckbox")
        self.verticalLayoutL.addWidget(self.favOnlyCheckbox)
        self.sortByComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.sortByComboBox.setObjectName("sortByComboBox")
        self.sortByComboBox.addItem("")
        self.sortByComboBox.addItem("")
        self.verticalLayoutL.addWidget(self.sortByComboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayoutR = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayoutR.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutR.setObjectName("verticalLayoutR")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.songTitleLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.songTitleLabel.setFont(font)
        self.songTitleLabel.setObjectName("songTitleLabel")
        self.gridLayout.addWidget(self.songTitleLabel, 0, 0, 1, 1)
        self.favButton = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.favButton.sizePolicy().hasHeightForWidth())
        self.favButton.setSizePolicy(sizePolicy)
        self.favButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.favButton.setObjectName("favButton")
        self.gridLayout.addWidget(self.favButton, 0, 1, 1, 1)
        self.songArtistLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.songArtistLabel.setFont(font)
        self.songArtistLabel.setObjectName("songArtistLabel")
        self.gridLayout.addWidget(self.songArtistLabel, 1, 0, 1, 1)
        self.verticalLayoutR.addLayout(self.gridLayout)
        self.songTabWidget = QtWidgets.QTabWidget(self.layoutWidget1)
        self.songTabWidget.setObjectName("songTabWidget")
        self.lyricsTab = QtWidgets.QWidget()
        self.lyricsTab.setObjectName("lyricsTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lyricsTab)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lyricsTextView = QtWidgets.QTextBrowser(self.lyricsTab)
        font = QtGui.QFont()
        font.setFamily("Overpass Mono")
        self.lyricsTextView.setFont(font)
        self.lyricsTextView.setObjectName("lyricsTextView")
        self.verticalLayout_4.addWidget(self.lyricsTextView)
        self.songTabWidget.addTab(self.lyricsTab, "")
        self.chordTab = QtWidgets.QWidget()
        self.chordTab.setObjectName("chordTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.chordTab)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chordComboBox = QtWidgets.QComboBox(self.chordTab)
        self.chordComboBox.setObjectName("chordComboBox")
        self.chordComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.chordComboBox)
        self.chordsTextView = QtWidgets.QTextBrowser(self.chordTab)
        font = QtGui.QFont()
        font.setFamily("Overpass Mono")
        self.chordsTextView.setFont(font)
        self.chordsTextView.setObjectName("chordsTextView")
        self.verticalLayout_3.addWidget(self.chordsTextView)
        self.addChordButton = QtWidgets.QPushButton(self.chordTab)
        self.addChordButton.setObjectName("addChordButton")
        self.verticalLayout_3.addWidget(self.addChordButton)
        self.songTabWidget.addTab(self.chordTab, "")
        self.verticalLayoutR.addWidget(self.songTabWidget)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuSong = QtWidgets.QMenu(self.menubar)
        self.menuSong.setObjectName("menuSong")
        self.menuChords = QtWidgets.QMenu(self.menubar)
        self.menuChords.setObjectName("menuChords")
        self.menuTranspose = QtWidgets.QMenu(self.menuChords)
        self.menuTranspose.setObjectName("menuTranspose")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuFont_Size = QtWidgets.QMenu(self.menuView)
        self.menuFont_Size.setObjectName("menuFont_Size")
        MainWindow.setMenuBar(self.menubar)
        self.lyricsToolBar = QtWidgets.QToolBar(MainWindow)
        self.lyricsToolBar.setMovable(False)
        self.lyricsToolBar.setIconSize(QtCore.QSize(24, 24))
        self.lyricsToolBar.setFloatable(False)
        self.lyricsToolBar.setObjectName("lyricsToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.lyricsToolBar)
        self.chordsToolBar = QtWidgets.QToolBar(MainWindow)
        self.chordsToolBar.setEnabled(True)
        self.chordsToolBar.setMovable(False)
        self.chordsToolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.chordsToolBar.setOrientation(QtCore.Qt.Horizontal)
        self.chordsToolBar.setIconSize(QtCore.QSize(24, 24))
        self.chordsToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.chordsToolBar.setFloatable(False)
        self.chordsToolBar.setObjectName("chordsToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.chordsToolBar)
        MainWindow.insertToolBarBreak(self.chordsToolBar)
        self.actionNewSong = QtWidgets.QAction(MainWindow)
        self.actionNewSong.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/assets/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewSong.setIcon(icon)
        self.actionNewSong.setObjectName("actionNewSong")
        self.actionEditSong = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI/assets/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditSong.setIcon(icon1)
        self.actionEditSong.setObjectName("actionEditSong")
        self.actionDeleteSong = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteSong.setIcon(icon2)
        self.actionDeleteSong.setObjectName("actionDeleteSong")
        self.actionAddChords = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/assets/addChords.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddChords.setIcon(icon3)
        self.actionAddChords.setObjectName("actionAddChords")
        self.actionEditChords = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/assets/editChords.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditChords.setIcon(icon4)
        self.actionEditChords.setObjectName("actionEditChords")
        self.actionDeleteChords = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI/assets/deleteChords.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteChords.setIcon(icon5)
        self.actionDeleteChords.setObjectName("actionDeleteChords")
        self.actionChordsChart = QtWidgets.QAction(MainWindow)
        self.actionChordsChart.setObjectName("actionChordsChart")
        self.actionTransposeUp = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("UI/assets/caret-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTransposeUp.setIcon(icon6)
        self.actionTransposeUp.setObjectName("actionTransposeUp")
        self.actionTransposeDown = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("UI/assets/caret-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTransposeDown.setIcon(icon7)
        self.actionTransposeDown.setObjectName("actionTransposeDown")
        self.actionTransposeReset = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.actionTransposeReset.setFont(font)
        self.actionTransposeReset.setObjectName("actionTransposeReset")
        self.actionDuplicateChords = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("UI/assets/dupChords.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuplicateChords.setIcon(icon8)
        self.actionDuplicateChords.setObjectName("actionDuplicateChords")
        self.actionFontBigger = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("UI/assets/increaseFont.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFontBigger.setIcon(icon9)
        self.actionFontBigger.setObjectName("actionFontBigger")
        self.actionFontSmaller = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("UI/assets/decreaseFont.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFontSmaller.setIcon(icon10)
        self.actionFontSmaller.setObjectName("actionFontSmaller")
        self.actionFontReset = QtWidgets.QAction(MainWindow)
        self.actionFontReset.setObjectName("actionFontReset")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("UI/assets/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon11)
        font = QtGui.QFont()
        self.actionRefresh.setFont(font)
        self.actionRefresh.setVisible(True)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuSong.addAction(self.actionNewSong)
        self.menuSong.addAction(self.actionEditSong)
        self.menuSong.addAction(self.actionDeleteSong)
        self.menuSong.addSeparator()
        self.menuSong.addAction(self.actionRefresh)
        self.menuTranspose.addAction(self.actionTransposeUp)
        self.menuTranspose.addAction(self.actionTransposeDown)
        self.menuChords.addAction(self.actionAddChords)
        self.menuChords.addAction(self.actionEditChords)
        self.menuChords.addAction(self.actionDeleteChords)
        self.menuChords.addAction(self.actionDuplicateChords)
        self.menuChords.addSeparator()
        self.menuChords.addAction(self.menuTranspose.menuAction())
        self.menuChords.addSeparator()
        self.menuChords.addAction(self.actionChordsChart)
        self.menuFont_Size.addAction(self.actionFontBigger)
        self.menuFont_Size.addAction(self.actionFontSmaller)
        self.menuFont_Size.addAction(self.actionFontReset)
        self.menuView.addAction(self.menuFont_Size.menuAction())
        self.menubar.addAction(self.menuSong.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuChords.menuAction())
        self.lyricsToolBar.addAction(self.actionRefresh)
        self.lyricsToolBar.addSeparator()
        self.lyricsToolBar.addAction(self.actionNewSong)
        self.lyricsToolBar.addAction(self.actionEditSong)
        self.lyricsToolBar.addAction(self.actionDeleteSong)
        self.lyricsToolBar.addSeparator()
        self.lyricsToolBar.addAction(self.actionFontBigger)
        self.lyricsToolBar.addAction(self.actionFontSmaller)
        self.chordsToolBar.addAction(self.actionRefresh)
        self.chordsToolBar.addSeparator()
        self.chordsToolBar.addAction(self.actionAddChords)
        self.chordsToolBar.addAction(self.actionDuplicateChords)
        self.chordsToolBar.addAction(self.actionEditChords)
        self.chordsToolBar.addAction(self.actionDeleteChords)
        self.chordsToolBar.addSeparator()
        self.chordsToolBar.addAction(self.actionFontBigger)
        self.chordsToolBar.addAction(self.actionFontSmaller)
        self.chordsToolBar.addSeparator()
        self.chordsToolBar.addAction(self.actionTransposeUp)
        self.chordsToolBar.addAction(self.actionTransposeReset)
        self.chordsToolBar.addAction(self.actionTransposeDown)
        self.chordsToolBar.addSeparator()
        self.chordsToolBar.addAction(self.actionChordsChart)

        self.retranslateUi(MainWindow)
        self.songTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChordsHouse"))
        self.labelSongs_2.setText(_translate("MainWindow", "Songs"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Type to search..."))
        self.favOnlyCheckbox.setText(_translate("MainWindow", "Favorites Songs Only"))
        self.sortByComboBox.setCurrentText(_translate("MainWindow", "sort by title"))
        self.sortByComboBox.setItemText(0, _translate("MainWindow", "sort by title"))
        self.sortByComboBox.setItemText(1, _translate("MainWindow", "sort by artist"))
        self.songTitleLabel.setText(_translate("MainWindow", "Song Title"))
        self.favButton.setToolTip(_translate("MainWindow", "add to favorite"))
        self.favButton.setText(_translate("MainWindow", "+ Fav"))
        self.songArtistLabel.setText(_translate("MainWindow", "Artist"))
        self.lyricsTextView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Overpass Mono\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.songTabWidget.setTabText(self.songTabWidget.indexOf(self.lyricsTab), _translate("MainWindow", "Lyrics"))
        self.chordComboBox.setItemText(0, _translate("MainWindow", "version 1"))
        self.chordsTextView.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Overpass Mono\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addChordButton.setText(_translate("MainWindow", "Add Chord"))
        self.songTabWidget.setTabText(self.songTabWidget.indexOf(self.chordTab), _translate("MainWindow", "Chords"))
        self.menuSong.setTitle(_translate("MainWindow", "Song"))
        self.menuChords.setTitle(_translate("MainWindow", "Chords"))
        self.menuTranspose.setTitle(_translate("MainWindow", "Transpose"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFont_Size.setTitle(_translate("MainWindow", "Font Size"))
        self.lyricsToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.chordsToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNewSong.setText(_translate("MainWindow", "New Song"))
        self.actionNewSong.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionEditSong.setText(_translate("MainWindow", "Edit Song"))
        self.actionEditSong.setShortcut(_translate("MainWindow", "Ctrl+Shift+E"))
        self.actionDeleteSong.setText(_translate("MainWindow", "Delete Song"))
        self.actionDeleteSong.setShortcut(_translate("MainWindow", "Ctrl+Shift+Backspace"))
        self.actionAddChords.setText(_translate("MainWindow", "New Chords"))
        self.actionAddChords.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionEditChords.setText(_translate("MainWindow", "Edit Chords"))
        self.actionEditChords.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDeleteChords.setText(_translate("MainWindow", "Delete Chords"))
        self.actionDeleteChords.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
        self.actionChordsChart.setText(_translate("MainWindow", "Chords Chart"))
        self.actionTransposeUp.setText(_translate("MainWindow", "+"))
        self.actionTransposeUp.setShortcut(_translate("MainWindow", "Ctrl+]"))
        self.actionTransposeDown.setText(_translate("MainWindow", "-"))
        self.actionTransposeDown.setShortcut(_translate("MainWindow", "Ctrl+["))
        self.actionTransposeReset.setText(_translate("MainWindow", "Reset"))
        self.actionTransposeReset.setIconText(_translate("MainWindow", "0"))
        self.actionTransposeReset.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionDuplicateChords.setText(_translate("MainWindow", "Duplicate Chords"))
        self.actionDuplicateChords.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionFontBigger.setText(_translate("MainWindow", "Bigger"))
        self.actionFontBigger.setToolTip(_translate("MainWindow", "Increase lyrics font size"))
        self.actionFontBigger.setShortcut(_translate("MainWindow", "Ctrl+."))
        self.actionFontSmaller.setText(_translate("MainWindow", "Smaller"))
        self.actionFontSmaller.setToolTip(_translate("MainWindow", "Decrease lyrics font size"))
        self.actionFontSmaller.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionFontReset.setText(_translate("MainWindow", "Default"))
        self.actionFontReset.setToolTip(_translate("MainWindow", "Reset font size to default"))
        self.actionFontReset.setShortcut(_translate("MainWindow", "Ctrl+/"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setIconText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
