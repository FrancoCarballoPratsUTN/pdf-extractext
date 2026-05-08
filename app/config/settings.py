import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings."""
    def __init__(self):
        self.host_db = os.getenv("MONGO_HOST")
        self.port_db = int(os.getenv("MONGO_PORT"))
        self.user_db = os.getenv("MONGO_USER")
        self.password_db = os.getenv("MONGO_PASSWORD")
        self.max_bytes = int(os.getenv("MAX_BYTES"))
        self.min_bytes = int(os.getenv("MIN_BYTES"))

settings = Settings()
