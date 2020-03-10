from main import LoginDialog


def onRegister(window: LoginDialog):
    mainWindow = window.mainWindow
    mainUi = mainWindow.ui

    def handleChange():
        window.close()
        mainUi.actionSign_Up.trigger()

    return handleChange
