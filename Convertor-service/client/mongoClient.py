import os
from pymongo import MongoClient
from gridfs import GridFS
from dotenv import load_dotenv
load_dotenv()


MONGO_URI = os.environ.get('MONGO_CONNECTION_STRING')
def get_client():
    return MongoClient(MONGO_URI)

def get_db(DB_NAME: str):
    client = get_client()
    return client[DB_NAME]

def get_gridfs(DB_NAME: str):
    db = get_db(DB_NAME)
    return GridFS(db)
