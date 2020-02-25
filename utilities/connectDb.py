import pymongo
import ssl


def create_db_connection():
    uri = "mongodb+srv://gigigi:gigigi@chordshouse-eazg8.mongodb.net/test?retryWrites=true&w=majority"
    try:
        client = pymongo.MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE, serverSelectionTimeoutMS=2500)
        client.test
    except:
        print('Error!')
    database = client.get_database('ChordsHouse')
    return database


def test():
    db = create_db_connection()
    coll = db.get_collection('Songs')
    songs = coll.find({}, {'title': 1, 'artist': 1})
    for s in songs:
        print(s['_id'])
        print(s['title'])
        print(s['artist'])
        print()


if __name__ == '__main__':
    test()
