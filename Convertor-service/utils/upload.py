from client.mongoClient import get_gridfs
import io
from datetime import datetime
from client.rabbitMQClient import publish_message

DB_NAME = "AUDIO_DB"
def upload(f):
    fs = get_gridfs(DB_NAME= DB_NAME)
    try:
        fid = fs.upload_from_stream(
            filename= f"{datetime.now()}.mp3",
            source=io.BytesIO(f),
            metadata={
                "content_type": "audio/mp3",
                "size": len(f),
                "upload_date": datetime.now()
            }
        )
    except Exception as err:
        print(err)
        return "internal server error, fs level", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None
    }

    #publish message to rmq
    try:
        publish_message(message)
    except Exception as err:
        print(err)
        return "internal server error, rmq level", 500
    
    return message, 200