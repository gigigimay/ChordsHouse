from bson.objectid import ObjectId
from utilities.connectDb import create_db_connection

_db = create_db_connection()
_songsCollection = _db.get_collection('Songs')
_chordsCollection = _db.get_collection('Chords')


def get_songs_list(sortby='title'):
    # result = list(_songsCollection.find({}))  # just in case :)
    if sortby == 'title':
        sort = {'lowerTitle': 1, 'lowerArtist': 1}
    elif sortby == 'artist':
        sort = {'lowerArtist': 1, 'lowerTitle': 1}
    result = list(_songsCollection.aggregate([
        {'$project': {
            '_id': 1,
            'title': 1,
            'artist': 1,
            'lyrics': 1,
            'lowerTitle': {'$toLower': '$title'},
            'lowerArtist': {'$toLower': '$artist'},
        }},
        {'$sort': sort}
    ]))
    return result


def get_song_data(songId):
    result = _songsCollection.find_one({'_id': songId})
    return result


def get_song_chords_list(songId):
    result = list(_chordsCollection.find({'songId': songId}))
    return result


def add_song(**song):
    result = _songsCollection.insert_one(song)
    print(f'inserted_id: {result.inserted_id}')
    return result.inserted_id


def edit_song(songId, **update):
    result = _songsCollection.update_one({'_id': ObjectId(songId)}, {'$set': update}, upsert=True)
    print(f'modified_count: {result.modified_count}')
    print(f'modified_count: {result.upserted_id}')


def delete_song(songId):
    chordResult = _chordsCollection.delete_many({'songId': songId})
    songResult = _songsCollection.delete_one({'_id': ObjectId(songId)})
    print(f'deleted_count: song = {songResult.deleted_count}, chords = {chordResult.deleted_count}')


def add_chords(**chord):
    result = _chordsCollection.insert_one(chord)
    print(f'inserted_id: {result.inserted_id}')
    return result.inserted_id


def edit_chords(chordsId, **update):
    result = _chordsCollection.update_one({'_id': ObjectId(chordsId)}, {'$set': update}, upsert=True)
    print(f'edit_chords - modified_count: {result.modified_count}')
    print(f'edit_chords - upserted_id: {result.upserted_id}')


def delete_chords(chordsId):
    result = _chordsCollection.delete_one({'_id': ObjectId(chordsId)})
    print(f'deleted_count: {result.deleted_count}')


if __name__ == '__main__':
    p = get_songs_list()
    print(p)
