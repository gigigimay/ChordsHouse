def onAccept(window):
    ui = window.ui
    def handleChange():
        window.close()

    return handleChange


def onCancel(window):
    def handleChange():
        window.close()
    return handleChange
