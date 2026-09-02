import logging

from app.config.settings import settings
from app.domain.entities.audit_log import AuditLog
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.domain.mappers.to_dto import audit_log_to_dict, to_audit_log_dto
from app.domain.repositories.audit_log_repository import AuditLogRepository

logger = logging.getLogger(__name__)


def _to_audit_logs(docs: list[dict]) -> list[AuditLog]:
    return [to_audit_log_dto({**doc, "_id": str(doc["_id"])}) for doc in docs]


class MongoAuditLogRepository(AuditLogRepository):
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
        data = audit_log_to_dict(audit_log)
        result = self._collection.insert_one(data)
        audit_log._id = str(result.inserted_id)
        logger.info(f"Audit log saved successfully with _id: {audit_log._id}")
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
        docs = list(cursor)
        result = _to_audit_logs(docs)
        logger.info(f"Retrieved {len(docs)} audit logs from the database.")

        return result

    def find_by_checksum(self, checksum: str) -> list[AuditLog]:
        """
        Finds audit logs by their checksum.
        Args:
            checksum (str): The checksum to search for.
        Returns:
            list[AuditLog]: A list of audit logs with the specified checksum,
            or an empty list if none are found.
        """
        cursor = self._collection.find({"checksum": checksum})
        docs = list(cursor)
        logger.info(f"Audit logs found with checksum {checksum}: {len(docs)}")

        if not docs:
            raise DocumentNotFoundError(
                "No audit logs found with the specified checksum."
            )

        return _to_audit_logs(docs)
