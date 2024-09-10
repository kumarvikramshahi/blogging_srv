import logging
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config import ConfigSettings


class MongoDbConnection:
    BloggingSrvDb: AsyncIOMotorDatabase = None
    Client: AsyncIOMotorClient = None

    def __init__(self) -> None:
        pass

    def Create(self) -> None:
        mongoUri = f"mongodb+srv://{ConfigSettings.MONGODB_USER}:{ConfigSettings.MONGODB_PASSWORD}@{ConfigSettings.MONGODB_HOST}/"
        self.client = AsyncIOMotorClient(mongoUri)
        self.BloggingSrvDb = self.client[ConfigSettings.MONGODB_NAME]
        logging.info("Connected to the MongoDB database!")

    def Close(self) -> None:
        self.client.close()
        logging.info("Closed Mongo Connection")
