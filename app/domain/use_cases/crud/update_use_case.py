from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
class UpdateDocumentUseCase:
    """Use case for updating a document in the repository."""
    def __init__(self):
        self._repository = MongoRepository()       
    
    def execute(self, document_checksum: str, updated_data: dict):
        updated_document = self._repository.update(document_checksum, updated_data)
        if not updated_document:
            raise ValueError("Document not found.")

        return updated_document