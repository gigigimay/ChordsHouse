from bson.objectid import ObjectId
from utilities.connectDb import create_db_connection

_db = create_db_connection()
_songsCollection = _db.get_collection('Songs')

def get_songs_list():
    songs = []
    result = _songsCollection.find({})
    for r in result:
        songs.append(r)
    return songs


def get_song_data(id):
    result = _songsCollection.find_one({ '_id': id })
    return result


def add_song(**song):
    result = _songsCollection.insert_one(song)
    print(f'inserted_id: {result.inserted_id}')
    return result.inserted_id


def edit_song(id, **update):
    result = _songsCollection.update_one({'_id': ObjectId(id)}, {'$set': update})
    print(f'modified_count: {result.modified_count}')


def delete_song(id):
    result = _songsCollection.delete_one({'_id': ObjectId(id)})
    print(f'deleted_count: {result.deleted_count}')


if __name__ == '__main__':
    print()
    # add_song(title='Stay', artist='Post Malone', lyrics='''''')
    # edit_song('5e5d0e4246a98a12056dcf33', title='')
