from fastapi import Depends
from client.mongoClient import get_async_gridfs, get_sync_db
import io
from datetime import datetime
from client.rabbitMQClient import publish_message

async def upload(f):
    fs = await get_async_gridfs()
    try:
        fid = await fs.upload_from_stream(
            filename= f"{datetime.now()}.mp4",
            source=io.BytesIO(f),
            metadata={
                "content_type": "video/mp4",
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