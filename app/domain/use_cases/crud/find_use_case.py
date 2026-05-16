from app.domain.entities.document import Document
class FindDocumentUseCase:
    """Use case for finding a document in the repository."""
    def __init__(self, repository):
        self._repository = repository

    def execute(self, document_checksum: str)-> Document:
        return self._repository.find_by_checksum(document_checksum)