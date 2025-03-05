from fastapi import Depends
from client.mongoClient import get_async_gridfs
import io
from datetime import datetime

async def upload(f):
    fs = await get_async_gridfs()
    try:
        fid = await fs.upload_from_stream(
            filename="sdsdsds",
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
    return message, 200