from client.mongoClient import get_gridfs
import io
from datetime import datetime
from client.rabbitMQClient import publish_message

DB_NAME = "AUDIO_DB"
def upload(f):
    fs = get_gridfs(DB_NAME= DB_NAME)
    try:
        data = f.read()
        fid = fs.put(data=data)
    except Exception as err:
        print(err)
        return "internal server error, fs level", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None
    }
    
    return message, 200