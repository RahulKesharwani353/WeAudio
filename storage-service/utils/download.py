from client.mongoClient import get_async_gridfs

DB_NAME = "AUDIO_DB"
async def download(file_id: str):
    fs = await get_async_gridfs(DB_NAME= DB_NAME)
    try:
        file = await fs.open_download_stream(file_id)
    except Exception as err:
        print(err)
        return "internal server error, fs level", 500

    return file, 200