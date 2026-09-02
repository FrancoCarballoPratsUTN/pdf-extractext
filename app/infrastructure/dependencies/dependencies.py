from app.config.settings import settings
from app.domain.contracts.document_converter import Converter
from app.domain.use_cases.audit.audit_decorator import AuditDecorator
from app.domain.use_cases.audit.find_audit_by_checksum_use_case import (
    FindAuditLogsByChecksumUseCase,
)
from app.domain.use_cases.audit.find_audit_use_case import FindAuditLogsUseCase
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.domain.use_cases.crud.delete_use_case import DeleteDocumentUseCase
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase
from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase
from app.infrastructure.converters.extract_text import ExtractText
from app.infrastructure.persistence.database.connection import mongo_connection
from app.infrastructure.persistence.repositories.mongo_audit_repository import (
    MongoAuditLogRepository,
)
from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository


def document_repository() -> MongoRepository:
    collection = mongo_connection.get_db
    return MongoRepository(collection)


def audit_repository() -> MongoAuditLogRepository:
    collection = mongo_connection.get_db
    return MongoAuditLogRepository(collection)


def text_extractor() -> Converter:
    """Factory function to create an instance of Converter."""
    return ExtractText()


def _wrap_with_audit(use_case, action: str, checksum_extractor):
    return AuditDecorator(
        use_case=use_case,
        audit_repo=audit_repository(),
        action=action,
        entity_type=settings.audit_entity_type,
        checksum_extractor=checksum_extractor,
    )


def get_find_document_use_case() -> FindDocumentUseCase:
    """Factory function to create an instance of FindDocumentUseCase."""

    return FindDocumentUseCase(document_repository())


def get_save_document_use_case() -> AuditDecorator:
    """Factory function to create an instance of SaveDocumentUseCase."""
    return _wrap_with_audit(
        SaveDocumentUseCase(document_repository()),
        action=settings.audit_save_action,
        checksum_extractor=lambda result, *args, **kwargs: args[0].checksum,
    )


def get_update_document_use_case() -> AuditDecorator:
    """Factory function to create an instance of UpdateDocumentUseCase."""
    return _wrap_with_audit(
        UpdateDocumentUseCase(document_repository()),
        action=settings.audit_update_action,
        checksum_extractor=lambda result, *args, **kwargs: args[0],
    )


def get_delete_document_use_case() -> AuditDecorator:
    """Factory function to create an instance of DeleteDocumentUseCase."""
    return _wrap_with_audit(
        DeleteDocumentUseCase(document_repository()),
        action=settings.audit_delete_action,
        checksum_extractor=lambda result, *args, **kwargs: args[0],
    )


def get_process_document_use_case() -> AuditDecorator:
    """Factory function to create an instance of ProcessDocumentUseCase."""
    return _wrap_with_audit(
        ProcessDocumentUseCase(text_extractor()),
        action=settings.audit_process_action,
        checksum_extractor=lambda result, *args, **kwargs: result.checksum,
    )


def get_find_audit_use_case() -> FindAuditLogsUseCase:
    """Factory function to create an instance of FindAuditLogsUseCase."""
    return FindAuditLogsUseCase(audit_repository())


def get_find_audit_by_checksum() -> FindAuditLogsByChecksumUseCase:
    """Factory function to create an instance of FindAuditLogsByChecksumUseCase."""
    return FindAuditLogsByChecksumUseCase(audit_repository())
