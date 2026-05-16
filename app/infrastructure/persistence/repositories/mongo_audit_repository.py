from app.domain.mappers.to_dto import to_audit_log_dto
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.config.settings import settings
from app.domain.repositories.audit_log_repository import Audit_LogRepository
from app.domain.entities.audit_log import Audit_Log

class MongoAuditLogRepository(Audit_LogRepository):
    def __init__(self, db):
        self._collection = db[settings.mongo_collection_audit_logs]

    def save(self, audit_log: Audit_Log) -> Audit_Log:
        """
        Saves an audit log to the database.
        Args:
            audit_log (Audit_Log): The audit log to save.
        Returns:
            Audit_Log: The saved audit log with an assigned ID.
        """
        result = self._collection.insert_one(audit_log.__dict__)
        audit_log.id = str(result.inserted_id)
        return audit_log

    def find_all(self, skip: int = 0, limit: int = 10) -> list[Audit_Log]:
        """ 
        Retrieves all audit logs from the database with pagination.
        Args:
            skip (int): The number of documents to skip.
            limit (int): The maximum number of documents to return.
        Returns:
            list[Audit_Log]: A list of audit logs.
        """
        cursor = self._collection.find().skip(skip).limit(limit)
        return [to_audit_log_dto(doc) for doc in list(cursor)]

    def find_by_checksum(self, checksum: str) -> list[Audit_Log]: 
        """
        Finds audit logs by their checksum.
        Args:
            checksum (str): The checksum to search for.
        Returns:
            list[Audit_Log]: A list of audit logs with the specified checksum, or an empty list if none are found.
        """
        cursor = self._collection.find({"checksum": checksum})
        docs = list(cursor)

        if not docs:
            raise DocumentNotFoundError("No audit logs found with the specified checksum.")
        
        return [to_audit_log_dto(doc) for doc in docs]  
        