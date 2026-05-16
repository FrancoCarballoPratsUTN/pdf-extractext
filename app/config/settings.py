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
        self.mongo_collection_file = os.getenv("MONGO_COLLECTION_FILE")
        self.mongo_collection_audit_logs = os.getenv("MONGO_COLLECTION_AUDIT_LOGS")
        self.audit_save_action = os.getenv("AUDIT_SAVE_ACTION")
        self.audit_update_action = os.getenv("AUDIT_UPDATE_ACTION")
        self.audit_delete_action = os.getenv("AUDIT_DELETE_ACTION")
        self.audit_process_action = os.getenv("AUDIT_PROCESS_ACTION")
        self.audit_entity_type = os.getenv("AUDIT_ENTITY_TYPE")

settings = Settings()
