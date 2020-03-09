from PyQt5.QtWidgets import QFileDialog


def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


def getCurrentChordsData(mainUi):
    if mainUi.currentChordsIndex > -1:
        return mainUi.allCurrentSongChords[mainUi.currentChordsIndex]


def setActionsDisabled(bool, actions):
    for a in actions:
        a.setDisabled(bool)


def setWidgetsVisible(bool, widgets):
    for w in widgets:
        w.show() if bool else w.hide()


def writeFile(path, text):
    with open(path, mode='w') as f:
        f.write(text)


def readFile(path):
    with open(path, mode='r') as f:
        return f.read()


def getSaveFileName(window, caption, defaultName):
    return QFileDialog.getSaveFileName(window, caption, f'{defaultName}.txt', filter='Text File(*.txt)')


def getOpenFileContent(window, caption):
    fileName = QFileDialog.getOpenFileName(window, caption, filter='Text File(*.txt)')
    if fileName[0]:
        return readFile(fileName[0])
