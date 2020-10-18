import os
from motor import motor_asyncio

DB_CONNECTION = None
DATABASE = None


def db_connection():
    global DB_CONNECTION
    if DB_CONNECTION is None:
        mongo_url = os.getenv('MONGO_URL')
        assert mongo_url
        DB_CONNECTION = motor_asyncio.AsyncIOMotorClient(mongo_url)
    return DB_CONNECTION


def db():
    global DATABASE
    if DATABASE is None:
        mongo_database = os.getenv('MONGO_DATABASE')
        assert mongo_database
        DATABASE = db_connection()[mongo_database]
    return DATABASE
