import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from gridfs import GridFS
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from dotenv import load_dotenv
load_dotenv()


MONGO_URI = os.environ.get('MONGO_CONNECTION_STRING')
DATABASE_NAME = "VIDEO_DB"

async def get_async_client():
    return AsyncIOMotorClient(MONGO_URI)

async def get_async_db(DB_NAME: str):
    client = await get_async_client()
    return client[DB_NAME]

async def get_async_gridfs(DB_NAME: str):
    db = await get_async_db(DB_NAME)
    # Use AsyncIOMotorGridFSBucket which is designed for Motor
    return AsyncIOMotorGridFSBucket(db)