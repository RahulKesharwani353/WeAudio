from client.mongoClient import get_gridfs

DB_NAME = "AUDIO_DB"
def upload(f):
    fs = get_gridfs(DB_NAME= DB_NAME)
    try:
        data = f.read()
        fid = fs.put(data=data)
    except Exception as err:
        print(err)
        return "internal server error, fs level", 500

    message = str(fid)
    
    return message