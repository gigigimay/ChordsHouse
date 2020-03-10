from utilities.utils import getCurrentChordsData
from utilities.text import getSongLabel, getInitialChords, addCopySuffix
from constants import ARTIST_PLACEHOLDER, CHORDS_PLACEHOLDER
from main import LoginDialog, RegisterDialog
from PyQt5.QtWidgets import QLineEdit


# ---------------------------- ui init ----------------------------
def initLyricsWindow(window, song=None):
    ui = window.ui
    ui.titleInput.setFocus()
    ui.currentSong = song
    if not song:
        ui.mode = 'add'
        ui.titleInput.setText('')
        ui.artistInput.setText('')
        ui.lyricsInput.setPlainText('')
        window.setWindowTitle('New Song')
        ui.dialogTitleLabel.setText('New Song')
    else:
        ui.mode = 'edit'
        ui.titleInput.setText(song['title'])
        ui.artistInput.setText(song['artist'])
        ui.lyricsInput.setPlainText(song['lyrics'])
        window.setWindowTitle('Edit Song')
        ui.dialogTitleLabel.setText('Edit Song')


def initChordsWindow(window, chords=None, duplicate=False):
    ui = window.ui
    song = window.mainWindow.ui.currentSong

    ui.chordsNameInput.setFocus()
    ui.currentChords = chords
    ui.currentSong = song
    ui.songTitleLabel.setText(song['title'])
    ui.songArtistLabel.setText(song['artist'] or ARTIST_PLACEHOLDER)
    if not chords:
        ui.mode = 'add'
        windowTitle = 'New Chords'
        chordsTitle = ''
        chordsBody = getInitialChords(song['lyrics'])
    elif duplicate:
        allChordsName = [c['title'] or CHORDS_PLACEHOLDER for c in window.mainWindow.ui.allCurrentSongChords]
        ui.mode = 'add'
        windowTitle = 'Duplicate Chords'
        chordsTitle = addCopySuffix(f"{chords['title'] or CHORDS_PLACEHOLDER}", allChordsName)
        chordsBody = chords['body']
    else:
        ui.mode = 'edit'
        windowTitle = 'Edit Chords'
        chordsTitle = chords['title']
        chordsBody = chords['body']
    ui.chordsNameInput.setText(chordsTitle)
    ui.lyricsInput.setPlainText(chordsBody)
    window.setWindowTitle(windowTitle)
    ui.dialogTitleLabel.setText(windowTitle)


def initDeleteSongDialog(window):
    ui = window.ui
    ui.mode = 'song'
    label = getSongLabel(window.mainWindow.ui.currentSong)
    ui.label.setText(f'ALL CHORDS IN THIS SONG WILL BE LOST.\n\nDelete this song?\n"{label}"')


def initDeleteChordsDialog(window):
    ui = window.ui
    ui.mode = 'chords'
    label = getSongLabel(window.mainWindow.ui.currentSong)
    currentChords = getCurrentChordsData(window.mainWindow.ui)
    chordName = currentChords['title'] or CHORDS_PLACEHOLDER
    ui.label.setText(f'Delete this chords?\n{label}\n\n" {chordName} "')


def initLoginDialog(window: LoginDialog, username=''):
    ui = window.ui
    ui.usernameInput.setText(username)
    ui.pwdInput.setText('')
    if username:
        ui.pwdInput.setFocus()
    else:
        ui.usernameInput.setFocus()
    window.show()


def initRegisterDialog(window: RegisterDialog, mode='register'):
    ui = window.ui
    ui.mode = mode
    if mode == 'register':
        label1 = 'Username'
        label2 = 'Password'
        label3 = 'Confirm Password'
        ui.usernameInput.setEchoMode(QLineEdit.Normal)
    elif mode == 'changePassword':
        label1 = 'Old Password'
        label2 = 'New Password'
        label3 = 'Confirm Password'
        ui.usernameInput.setEchoMode(QLineEdit.Password)
    ui.label.setText(label1)
    ui.label_2.setText(label2)
    ui.label_3.setText(label3)
    ui.usernameInput.setText('')
    ui.pwdInput.setText('')
    ui.pwdInput2.setText('')
    ui.usernameInput.setFocus()
    window.show()
