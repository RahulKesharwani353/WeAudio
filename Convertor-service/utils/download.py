from client.mongoClient import get_gridfs
from bson.objectid import ObjectId

DB_NAME = "VIDEO_DB"
def download(file_id: str):
    fs = get_gridfs(DB_NAME= DB_NAME)
    try:
        file = fs.get(ObjectId(file_id))
    except Exception as err:
        print(err)
        return "internal server error, fs level", 500

    return file, 200