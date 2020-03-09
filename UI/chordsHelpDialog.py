# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chordsHelpDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chordsHelpDialog(object):
    def setupUi(self, chordsHelpDialog):
        chordsHelpDialog.setObjectName("chordsHelpDialog")
        chordsHelpDialog.resize(446, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(chordsHelpDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(chordsHelpDialog)
        font = QtGui.QFont()
        font.setFamily("Overpass Mono")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(chordsHelpDialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(chordsHelpDialog)
        QtCore.QMetaObject.connectSlotsByName(chordsHelpDialog)

    def retranslateUi(self, chordsHelpDialog):
        _translate = QtCore.QCoreApplication.translate
        chordsHelpDialog.setWindowTitle(_translate("chordsHelpDialog", "Help"))
        self.textBrowser.setHtml(_translate("chordsHelpDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Overpass Mono\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">How to write chords</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">- All </span><span style=\" font-weight:600; color:#149a8b;\">chords</span><span style=\" color:#000000;\"> lines must have </span><span style=\" font-weight:600; color:#149a8b;\">:</span><span style=\" color:#000000;\"> prefix.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">- All </span><span style=\" font-weight:600; color:#149a8b;\">lyrics</span><span style=\" color:#000000;\"> lines must have </span><span style=\" font-weight:600; color:#149a8b;\">&gt;</span><span style=\" color:#000000;\"> prefix.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">- All prefixes mush be followed by a space</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#000000;\">example:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f3f3f3;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f3f3f3;\"><span style=\" font-weight:600; color:#149a8b;\">:</span><span style=\" color:#000000;\"> </span><span style=\" font-weight:600; color:#000000;\">Em</span><span style=\" color:#000000;\">       </span><span style=\" font-weight:600; color:#000000;\">C</span><span style=\" color:#000000;\">                </span><span style=\" font-weight:600; color:#000000;\">G</span><span style=\" color:#000000;\">                </span><span style=\" font-weight:600; color:#000000;\">D/F#</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f3f3f3;\"><span style=\" font-weight:600; color:#149a8b;\">&gt;</span><span style=\" color:#000000;\"> Another head hangs lowly, child is slowly taken</span> </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f3f3f3;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("chordsHelpDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chordsHelpDialog = QtWidgets.QDialog()
    ui = Ui_chordsHelpDialog()
    ui.setupUi(chordsHelpDialog)
    chordsHelpDialog.show()
    sys.exit(app.exec_())
