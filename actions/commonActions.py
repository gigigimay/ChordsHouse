def onCancel(window):
    def handleChange():
        window.close()

    return handleChange