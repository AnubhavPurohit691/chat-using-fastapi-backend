from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from pymongo import MongoClient
from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    # MongoDB URI (make sure MongoDB is running and accessible)
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db: str = "realtimechat"  # Your database name

    class Config:
        env_file = ".env"

# Create an instance of Settings
settings = Settings()

# Create the database client
client = AsyncIOMotorClient(settings.mongodb_uri)

# Get the database instance
db = client[settings.mongodb_db]

# Dependency to inject the database instance into routes
def get_db():
    return db