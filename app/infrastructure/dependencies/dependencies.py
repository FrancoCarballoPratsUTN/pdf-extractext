from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.domain.use_cases.crud.delete_use_case import DeleteDocumentUseCase
from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
from app.infrastructure.persistence.database.connection import mongo_connection
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase
from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase


def repository():
    collection = mongo_connection.collection
    return MongoRepository(collection)

def get_find_document_use_case():
    """Factory function to create an instance of FindDocumentUseCase."""

    return FindDocumentUseCase(repository())

def get_save_document_use_case():
    """Factory function to create an instance of SaveDocumentUseCase."""
    return SaveDocumentUseCase(repository())

def get_update_document_use_case():
    """Factory function to create an instance of UpdateDocumentUseCase."""
    return UpdateDocumentUseCase(repository())

def get_delete_document_use_case():
    """Factory function to create an instance of DeleteDocumentUseCase."""
    return DeleteDocumentUseCase(repository())

def get_process_document_use_case():
    """Factory function to create an instance of ProcessDocumentUseCase."""
    return ProcessDocumentUseCase()