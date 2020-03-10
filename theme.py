from PyQt5 import QtGui, QtCore

grey = QtGui.QColor(50, 53, 55)

def setTheme(app):
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, grey)
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, grey.darker())
    palette.setColor(QtGui.QPalette.AlternateBase, grey)
    palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(70, 70, 70))
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, grey)
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.blue)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(121, 220, 210))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)