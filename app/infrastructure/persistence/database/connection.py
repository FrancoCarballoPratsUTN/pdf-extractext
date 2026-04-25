import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnection:
    def __init__(self):
        self._client = None
        self._db = None

    def connect(self):
        """Connects to the MongoDB database using environment variables for configuration."""
        if self._client is None:
            try:
                host = os.getenv("MONGO_HOST")
                port = int(os.getenv("MONGO_PORT", 27017))
                user = os.getenv("MONGO_USER")
                password = os.getenv("MONGO_PASSWORD")

                self._client = MongoClient(
                    host=host,
                    port=port,
                    username=user,
                    password=password,
                    authSource="admin",
                    serverSelectionTimeoutMS=5000 
                )
                self._client.admin.command('ping')
                
                self._db = self._client['pdf_extractext']
                self._ensure_indexes()
                
            except ConnectionFailure as e:
                print(f"Connection failed: {e}")
                raise

    def _ensure_indexes(self):
        """Ensures that the necessary indexes are created on the collection."""
        self._db["file"].create_index("checksum", unique=True)

    @property
    def collection(self):
        if self._db is None:
            self.connect()
        return self._db["file"]

    def close(self):
        """Closes the MongoDB connection."""
        if self._client:
            self._client.close()
            self._client = None
            self._db = None

mongo_connection = MongoDBConnection()