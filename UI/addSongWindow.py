# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSongDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import setupUi


class Ui_AddSong(object):
    def setupUi(self, AddSong):
        AddSong.setObjectName("AddSong")
        AddSong.resize(420, 490)
        self.formLayout = QtWidgets.QFormLayout(AddSong)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.dialogTitleLabel = QtWidgets.QLabel(AddSong)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dialogTitleLabel.setFont(font)
        self.dialogTitleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dialogTitleLabel.setObjectName("dialogTitleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dialogTitleLabel)
        self.titleLabel = QtWidgets.QLabel(AddSong)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleInput = QtWidgets.QLineEdit(AddSong)
        self.titleInput.setText("")
        self.titleInput.setObjectName("titleInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titleInput)
        self.artistLabel = QtWidgets.QLabel(AddSong)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistInput = QtWidgets.QLineEdit(AddSong)
        self.artistInput.setText("")
        self.artistInput.setObjectName("artistInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.artistInput)
        self.lyricsLabel = QtWidgets.QLabel(AddSong)
        self.lyricsLabel.setObjectName("lyricsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lyricsLabel)
        self.lyricsInput = QtWidgets.QPlainTextEdit(AddSong)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lyricsInput.sizePolicy().hasHeightForWidth())
        self.lyricsInput.setSizePolicy(sizePolicy)
        self.lyricsInput.setMinimumSize(QtCore.QSize(200, 200))
        self.lyricsInput.setObjectName("lyricsInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lyricsInput)
        self.importButton = QtWidgets.QPushButton(AddSong)
        self.importButton.setObjectName("importButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.importButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddSong)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(AddSong)
        setupUi.addSongWindow(self)
        QtCore.QMetaObject.connectSlotsByName(AddSong)

    def retranslateUi(self, AddSong):
        _translate = QtCore.QCoreApplication.translate
        AddSong.setWindowTitle(_translate("AddSong", "Form"))
        self.dialogTitleLabel.setText(_translate("AddSong", "Add new Song"))
        self.titleLabel.setText(_translate("AddSong", "Song Title"))
        self.artistLabel.setText(_translate("AddSong", "Artist"))
        self.lyricsLabel.setText(_translate("AddSong", "Lyrics"))
        self.importButton.setText(_translate("AddSong", "Import from file..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddSong = QtWidgets.QWidget()
    ui = Ui_AddSong()
    ui.setupUi(AddSong)
    AddSong.show()
    sys.exit(app.exec_())
