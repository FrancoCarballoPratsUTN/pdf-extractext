from app.domain.entities.document import Document

class SaveDocumentUseCase:
    """Use case for saving a document to the repository."""
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, file: Document):
        return self._repository.save(file)