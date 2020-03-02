# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lyricsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LyricsWindow(object):
    def setupUi(self, LyricsWindow):
        LyricsWindow.setObjectName("LyricsWindow")
        LyricsWindow.resize(600, 450)
        self.formLayout = QtWidgets.QFormLayout(LyricsWindow)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(LyricsWindow)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleInput = QtWidgets.QLineEdit(LyricsWindow)
        self.titleInput.setText("")
        self.titleInput.setObjectName("titleInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleInput)
        self.artistLabel = QtWidgets.QLabel(LyricsWindow)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistInput = QtWidgets.QLineEdit(LyricsWindow)
        self.artistInput.setText("")
        self.artistInput.setObjectName("artistInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.artistInput)
        self.lyricsLabel = QtWidgets.QLabel(LyricsWindow)
        self.lyricsLabel.setObjectName("lyricsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel)
        self.lyricsInput = QtWidgets.QPlainTextEdit(LyricsWindow)
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
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lyricsInput)
        self.importButton = QtWidgets.QPushButton(LyricsWindow)
        self.importButton.setObjectName("importButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.importButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(LyricsWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.dialogTitleLabel = QtWidgets.QLabel(LyricsWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dialogTitleLabel.setFont(font)
        self.dialogTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dialogTitleLabel.setObjectName("dialogTitleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogTitleLabel)

        self.retranslateUi(LyricsWindow)
        QtCore.QMetaObject.connectSlotsByName(LyricsWindow)

    def retranslateUi(self, LyricsWindow):
        _translate = QtCore.QCoreApplication.translate
        LyricsWindow.setWindowTitle(_translate("LyricsWindow", "New Song"))
        self.titleLabel.setText(_translate("LyricsWindow", "Title*"))
        self.artistLabel.setText(_translate("LyricsWindow", "Artist"))
        self.lyricsLabel.setText(_translate("LyricsWindow", "Lyrics*"))
        self.importButton.setText(_translate("LyricsWindow", "Import from file..."))
        self.dialogTitleLabel.setText(_translate("LyricsWindow", "New Song"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LyricsWindow = QtWidgets.QWidget()
    ui = Ui_LyricsWindow()
    ui.setupUi(LyricsWindow)
    LyricsWindow.show()
    sys.exit(app.exec_())
