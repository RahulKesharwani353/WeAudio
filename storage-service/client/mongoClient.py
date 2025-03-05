import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from gridfs import GridFS
from motor.motor_asyncio import AsyncIOMotorGridFSBucket


MONGO_URI = os.environ.get('MONGO_CONNECTION_STRING')
DATABASE_NAME = "VIDEO_DB"

# Synchronous client (for use outside of FastAPI routes)
def get_sync_client():
    return MongoClient(MONGO_URI)

def get_sync_db():
    client = get_sync_client()
    return client[DATABASE_NAME]

def get_sync_gridfs():
    db = get_sync_db()
    return GridFS(db)

# Asynchronous client (for use within FastAPI routes)
async def get_async_client():
    return AsyncIOMotorClient(MONGO_URI)

async def get_async_db():
    client = await get_async_client()
    return client[DATABASE_NAME]

async def get_async_gridfs():
    db = await get_async_db()
    # Use AsyncIOMotorGridFSBucket which is designed for Motor
    return AsyncIOMotorGridFSBucket(db)