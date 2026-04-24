from app.infrastructure.persistence.repositories.mongo_repository import MongoRepository
from app.domain.entities.document import Document

class SaveDocumentUseCase:
    """Use case for saving a document to the repository."""
    def __init__(self):
        self._repository = MongoRepository()
    
    def execute(self, file: Document):
        return self._repository.save(file)