import logging

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from app.config.settings import settings

logger = logging.getLogger(__name__)

class MongoDBConnection:
    def __init__(self):
        self._client = None
        self._db = None

    def connect(self):
        """Connects to the MongoDB database using environment variables for configuration."""
        if self._client is None:
            try:
                host = settings.host_db
                port = settings.port_db
                user = settings.user_db
                password = settings.password_db
                self._client = MongoClient(
                    host=host,
                    port=port,
                    username=user,
                    password=password,
                    authSource="admin",
                    serverSelectionTimeoutMS=5000
                )
                self._db = self._client[settings.mongo_client]
                self._ensure_indexes()
                logger.info("Connected to MongoDB successfully.")
            except ConnectionFailure as e:
                logger.critical(f"Connection failed: {e}", exc_info=True)
                raise

    def _ensure_indexes(self):
        """Ensures that the necessary indexes are created on the collection."""
        self._db[settings.mongo_collection_file].create_index("checksum", unique=True)

    @property
    def get_db(self):
        if self._db is None:
            self.connect()
        return self._db

    def close(self):
        """Closes the MongoDB connection."""
        if self._client:
            self._client.close()
            self._client = None
            self._db = None
            logger.info("MongoDB connection closed.")

mongo_connection = MongoDBConnection()
