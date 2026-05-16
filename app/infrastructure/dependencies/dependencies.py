from app.config.settings import settings
from app.domain.use_cases.audit.audit_decorator import AuditDecorator
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.domain.use_cases.crud.delete_use_case import DeleteDocumentUseCase
from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
from app.infrastructure.persistence.database.connection import mongo_connection
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase
from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase
from app.domain.use_cases.audit.find_audit_use_case import FindAuditLogsUseCase
from app.domain.use_cases.audit.find_audit_by_checksum_use_case import FindAuditLogsByChecksumUseCase
from app.infrastructure.persistence.repositories.mongo_audit_repository import MongoAuditLogRepository


def document_repository() -> MongoRepository:
    collection = mongo_connection.get_db
    return MongoRepository(collection)

def audit_repository() -> MongoAuditLogRepository:
    collection = mongo_connection.get_db
    return MongoAuditLogRepository(collection)

def get_find_document_use_case() -> FindDocumentUseCase:
    """Factory function to create an instance of FindDocumentUseCase."""

    return FindDocumentUseCase(document_repository())

def get_save_document_use_case() -> SaveDocumentUseCase:
    """Factory function to create an instance of SaveDocumentUseCase."""
    repo = document_repository()          
    audit_repo = audit_repository()  
    use_case = SaveDocumentUseCase(repo)
    return AuditDecorator(use_case=use_case, audit_repo=audit_repo, action=settings.audit_save_action, entity_type=settings.audit_entity_type)

def get_update_document_use_case() -> UpdateDocumentUseCase:
    """Factory function to create an instance of UpdateDocumentUseCase."""
    repo = document_repository()          
    audit_repo = audit_repository()  
    use_case = UpdateDocumentUseCase(repo)
    return AuditDecorator(use_case=use_case, audit_repo=audit_repo, action=settings.audit_update_action, entity_type=settings.audit_entity_type)

def get_delete_document_use_case() -> DeleteDocumentUseCase:
    """Factory function to create an instance of DeleteDocumentUseCase."""
    repo = document_repository()          
    audit_repo = audit_repository()  
    use_case = DeleteDocumentUseCase(repo)
    return AuditDecorator(use_case=use_case, audit_repo=audit_repo, action=settings.audit_delete_action, entity_type=settings.audit_entity_type)

def get_process_document_use_case()-> ProcessDocumentUseCase:
    """Factory function to create an instance of ProcessDocumentUseCase."""
    audit_repo = audit_repository()  
    use_case = ProcessDocumentUseCase()
    return AuditDecorator(use_case=use_case, audit_repo=audit_repo, action=settings.audit_process_action, entity_type=settings.audit_entity_type)

def get_find_audit_use_case() -> FindAuditLogsUseCase:
    """Factory function to create an instance of FindAuditLogsUseCase."""
    return FindAuditLogsUseCase(audit_repository())

def get_find_audit_by_checksum() -> FindAuditLogsByChecksumUseCase:
    """Factory function to create an instance of FindAuditLogsByChecksumUseCase."""
    return FindAuditLogsByChecksumUseCase(audit_repository())

