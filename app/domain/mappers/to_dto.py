from app.domain.entities.audit_log import Audit_Log
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

def to_audit_log_dto(audit_log: dict) -> Audit_Log:
    """Converts a dictionary audit log to an Audit_Log DTO.
    Args:
        audit_log (dict): The dictionary audit log to convert.
    Returns:
        Audit_Log: The converted Audit_Log DTO.
    """
    return Audit_Log(
            action=audit_log.get("action"),
            entity_type=audit_log.get("entity_type"),
            checksum=audit_log.get("checksum"),
            details=audit_log.get("details"),
            performed_at=audit_log.get("performed_at"),
            id=audit_log.get("id")
        )