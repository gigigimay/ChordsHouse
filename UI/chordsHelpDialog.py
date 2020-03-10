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
        chordsHelpDialog.resize(466, 248)
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">How to write chords</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">- All </span><span style=\" font-weight:600; color:#4ee6d3;\">chords</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">lines must have </span><span style=\" font-weight:600; color:#4ee6d3;\">:</span><span style=\" color:#ffffff;\"> prefix.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">- All </span><span style=\" font-weight:600; color:#4ee6d3;\">lyrics</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">lines must have</span><span style=\" color:#000000;\"> </span><span style=\" font-weight:600; color:#149a8b;\">&gt;</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">prefix.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">- All prefixes mush be followed by a space</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#4ee6d3;\">example</span><span style=\" font-size:18pt; color:#0094b6;\">:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2d2d2d;\"><span style=\" font-weight:600; color:#4ee6d3;\">:</span><span style=\" color:#000000;\"> </span><span style=\" font-weight:600; color:#ffffff;\">Em</span><span style=\" color:#ffffff;\">       </span><span style=\" font-weight:600; color:#ffffff;\">C</span><span style=\" color:#ffffff;\">                </span><span style=\" font-weight:600; color:#ffffff;\">G</span><span style=\" color:#ffffff;\">                </span><span style=\" font-weight:600; color:#ffffff;\">D/F#</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2d2d2d;\"><span style=\" font-weight:600; color:#4ee6d3;\">&gt;</span><span style=\" color:#4ee6d3;\"> </span><span style=\" color:#ffffff;\">Another head hangs lowly, child is slowly taken </span></p></body></html>"))
        self.pushButton.setText(_translate("chordsHelpDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chordsHelpDialog = QtWidgets.QDialog()
    ui = Ui_chordsHelpDialog()
    ui.setupUi(chordsHelpDialog)
    chordsHelpDialog.show()
    sys.exit(app.exec_())
