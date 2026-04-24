from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository

class DeleteDocumentUseCase:
    """Use case for deleting a document from the repository."""
    def __init__(self):
        self._repository = MongoRepository()

    def execute(self, document_checksum: str):
        return self._repository.delete(document_checksum)