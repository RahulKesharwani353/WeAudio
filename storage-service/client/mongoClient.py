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

async def get_async_db():
    client = await get_async_client()
    return client[DATABASE_NAME]

async def get_async_gridfs():
    db = await get_async_db()
    # Use AsyncIOMotorGridFSBucket which is designed for Motor
    return AsyncIOMotorGridFSBucket(db)