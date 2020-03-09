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
