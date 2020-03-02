import constants as const
from PyQt5 import QtWidgets
from service import get_songs_list
from utilities.utils import getSongLabel


def renderLyrics(ui, text):
    lines = text.splitlines()
    result = []
    i = 0
    for line in lines:
        if line:
            div = f'<div class="{"odd" if i % 2 else "even"}">{line}</div>'
            i += 1
        else:
            div = '<div> </div>'
            i = 0
        result.append(div)
    newText = ''.join(result)
    size = ui.lyricsFontSize
    style = f'''body {{
            white-space: pre-wrap;
            font-size:{size}pt;
            font-family:'Overpass Mono';
            line-height: 80%;
        }}
        .even, .odd {{
            margin: {size / 2}px 0;
        }}
        .odd {{
            background-color: #f3f3f3;
        }}'''
    return f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        <html><head><style type="text/css">{style}</style></head>
        <body>{newText}</body></html>'''


def updateSongDetail(ui):
    song = ui.currentSong
    ui.songTitleLabel.setText(song['title'])
    ui.songArtistLabel.setText(song['artist'] or '(Unknown Artist)')
    ui.lyricsTextView.setHtml(renderLyrics(ui, song['lyrics']))


def setCurrentSong(ui, song):
    ui.currentSong = song
    updateSongDetail(ui)


def renderSongItems(ui, songs):
    ui.songList.clear()
    for i, song in enumerate(songs):
        item = QtWidgets.QListWidgetItem()
        item.setText(getSongLabel(song))
        item.setData(const.SONG_ITEM_DATA_INDEX, song)
        ui.songList.addItem(item)


def setAllSongs(ui, songs):
    ui.allSongs = songs
    renderSongItems(ui, ui.allSongs)


def refreshSongList(ui):
    # refresh song list
    newAllSongs = get_songs_list()
    ui.allSongs = newAllSongs
    renderSongItems(ui, ui.allSongs)

    # refresh current song
    prevSongId = ui.currentSong['_id']
    matches = list(filter(lambda song: song['_id'] == prevSongId, newAllSongs))
    # refresh the song detail
    newCurrentSong = matches[0] if matches else newAllSongs[0]
    setCurrentSong(ui, newCurrentSong)
    # reselect the song in songList widget
    index = newAllSongs.index(newCurrentSong)
    ui.songList.setCurrentRow(index)

    # TODO: clear search inputs OR do the search again


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
        ui.titleInput.setFocus()
        ui.titleInput.setText(song['title'])
        ui.artistInput.setText(song['artist'])
        ui.lyricsInput.setPlainText(song['lyrics'])
        window.setWindowTitle('Edit Song')
        ui.dialogTitleLabel.setText('Edit Song')


def initDeleteDialog(window):
    ui = window.ui
    ui.mode = 'song'
    label = getSongLabel(window.mainWindow.ui.currentSong)
    ui.label.setText(f'Confirm Deletion?\n{label}')
