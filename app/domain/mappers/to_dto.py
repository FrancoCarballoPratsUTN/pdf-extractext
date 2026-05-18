from app.domain.entities.audit_log import AuditLog
from app.domain.entities.document import Document

def to_document_dto(document: dict) -> Document:
    """Converts a dictionary document to a Document DTO.
    Args:        document (dict): The dictionary document to convert.
    Returns:        Document: The converted Document DTO.
    """
    return Document(
        file_name=document.get("file_name"),
        checksum=document.get("checksum"),
        text=document.get("text"),
        date=document.get("date")
    )

def to_audit_log_dto(audit_log: dict) -> AuditLog:
    """Converts a dictionary audit log to an AuditLog DTO.
    Args:
        audit_log (dict): The dictionary audit log to convert.
    Returns:
        AuditLog: The converted AuditLog DTO.
    """
    return AuditLog(
            action=audit_log.get("action"),
            entity_type=audit_log.get("entity_type"),
            checksum=audit_log.get("checksum"),
            details=audit_log.get("details"),
            performed_at=audit_log.get("performed_at"),
            _id=audit_log.get("_id")
        )