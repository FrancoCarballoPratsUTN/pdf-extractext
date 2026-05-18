from app.domain.mappers.to_dto import to_audit_log_dto
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.config.settings import settings
from app.domain.repositories.audit_log_repository import Audit_LogRepository
from app.domain.entities.audit_log import AuditLog

class MongoAuditLogRepository(Audit_LogRepository):
    def __init__(self, db):
        self._collection = db[settings.mongo_collection_audit_logs]

    def save(self, audit_log: AuditLog) -> AuditLog:
        """
        Saves an audit log to the database.
        Args:
            audit_log (AuditLog): The audit log to save.
        Returns:
            AuditLog: The saved audit log with an assigned _id.
        """
        data = {"action": audit_log.action,
                "entity_type": audit_log.entity_type,
                "checksum": audit_log.checksum,
                "details": audit_log.details,
                "performed_at": audit_log.performed_at}

        result = self._collection.insert_one(data)
        audit_log._id = str(result.inserted_id)
        return audit_log

    def find_all(self, skip: int = 0, limit: int = 10) -> list[AuditLog]:
        """ 
        Retrieves all audit logs from the database with pagination.
        Args:
            skip (int): The number of documents to skip.
            limit (int): The maximum number of documents to return.
        Returns:
            list[AuditLog]: A list of audit logs.
        """
        cursor = self._collection.find().skip(skip).limit(limit)

        return [to_audit_log_dto({**doc, "_id": str(doc["_id"])}) for doc in cursor]


    def find_by_checksum(self, checksum: str) -> list[AuditLog]: 
        """
        Finds audit logs by their checksum.
        Args:
            checksum (str): The checksum to search for.
        Returns:
            list[AuditLog]: A list of audit logs with the specified checksum, or an empty list if none are found.
        """
        cursor = self._collection.find({"checksum": checksum})
        docs = list(cursor)

        if not docs:
            raise DocumentNotFoundError("No audit logs found with the specified checksum.")
        
        return [to_audit_log_dto({**doc, "_id": str(doc["_id"])}) for doc in docs]  
        