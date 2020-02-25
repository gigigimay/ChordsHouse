from utilities.connectDb import create_db_connection


def get_songs_list():
    db = create_db_connection()
    songsCollection = db.get_collection('Songs')
    songs = []
    result = songsCollection.find({})
    for r in result:
        songs.append(r)
    return songs


def get_song_data(id):
    db = create_db_connection()
    songsCollection = db.get_collection('Songs')
    result = songsCollection.find_one({ '_id': id })
    return result