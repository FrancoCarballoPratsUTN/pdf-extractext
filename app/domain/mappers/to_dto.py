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
def document_to_dict(document: Document) -> dict:
    """Converts a Document DTO to a dictionary.
    Args:
        document (Document): The Document DTO to convert.
    Returns:
        dict: The converted dictionary representation of the Document.
    """
    return {
        "file_name": document.file_name,
        "checksum": document.checksum,
        "text": document.text,
        "date": document.date
    }

def audit_log_to_dict(audit_log: AuditLog) -> dict:
    """Converts an AuditLog DTO to a dictionary.
    Args:
        audit_log (AuditLog): The AuditLog DTO to convert.
    Returns:
        dict: The converted dictionary representation of the AuditLog.
    """
    return {
        "action": audit_log.action,
        "entity_type": audit_log.entity_type,
        "checksum": audit_log.checksum,
        "details": audit_log.details,
        "performed_at": audit_log.performed_at,
    }
