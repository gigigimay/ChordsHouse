# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chordsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChordsWindow(object):
    def setupUi(self, ChordsWindow):
        ChordsWindow.setObjectName("ChordsWindow")
        ChordsWindow.resize(600, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChordsWindow.sizePolicy().hasHeightForWidth())
        ChordsWindow.setSizePolicy(sizePolicy)
        self.formLayout = QtWidgets.QFormLayout(ChordsWindow)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.dialogTitleLabel = QtWidgets.QLabel(ChordsWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dialogTitleLabel.setFont(font)
        self.dialogTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dialogTitleLabel.setObjectName("dialogTitleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogTitleLabel)
        self.lyricsLabel_5 = QtWidgets.QLabel(ChordsWindow)
        self.lyricsLabel_5.setObjectName("lyricsLabel_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel_5)
        self.songTitleLabel = QtWidgets.QLabel(ChordsWindow)
        self.songTitleLabel.setObjectName("songTitleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.songTitleLabel)
        self.lyricsLabel_4 = QtWidgets.QLabel(ChordsWindow)
        self.lyricsLabel_4.setObjectName("lyricsLabel_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel_4)
        self.songArtistLabel = QtWidgets.QLabel(ChordsWindow)
        self.songArtistLabel.setObjectName("songArtistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.songArtistLabel)
        self.lyricsLabel_2 = QtWidgets.QLabel(ChordsWindow)
        self.lyricsLabel_2.setObjectName("lyricsLabel_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel_2)
        self.chordsNameInput = QtWidgets.QLineEdit(ChordsWindow)
        self.chordsNameInput.setObjectName("chordsNameInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chordsNameInput)
        self.lyricsLabel_3 = QtWidgets.QLabel(ChordsWindow)
        self.lyricsLabel_3.setObjectName("lyricsLabel_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel_3)
        self.lyricsInput = QtWidgets.QPlainTextEdit(ChordsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lyricsInput.sizePolicy().hasHeightForWidth())
        self.lyricsInput.setSizePolicy(sizePolicy)
        self.lyricsInput.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Overpass Mono")
        font.setKerning(True)
        self.lyricsInput.setFont(font)
        self.lyricsInput.setPlainText("")
        self.lyricsInput.setObjectName("lyricsInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lyricsInput)
        self.importButton = QtWidgets.QPushButton(ChordsWindow)
        self.importButton.setObjectName("importButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.importButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChordsWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(ChordsWindow)
        QtCore.QMetaObject.connectSlotsByName(ChordsWindow)

    def retranslateUi(self, ChordsWindow):
        _translate = QtCore.QCoreApplication.translate
        ChordsWindow.setWindowTitle(_translate("ChordsWindow", "New Chords"))
        self.dialogTitleLabel.setText(_translate("ChordsWindow", "New Chords"))
        self.lyricsLabel_5.setText(_translate("ChordsWindow", "Title"))
        self.songTitleLabel.setText(_translate("ChordsWindow", "Title"))
        self.lyricsLabel_4.setText(_translate("ChordsWindow", "Artist"))
        self.songArtistLabel.setText(_translate("ChordsWindow", "Artist"))
        self.lyricsLabel_2.setText(_translate("ChordsWindow", "Chords Name"))
        self.chordsNameInput.setText(_translate("ChordsWindow", "version1"))
        self.lyricsLabel_3.setText(_translate("ChordsWindow", "Chords*"))
        self.importButton.setText(_translate("ChordsWindow", "Import from file..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChordsWindow = QtWidgets.QWidget()
    ui = Ui_ChordsWindow()
    ui.setupUi(ChordsWindow)
    ChordsWindow.show()
    sys.exit(app.exec_())
