
class DeleteDocumentUseCase:
    """Use case for deleting a document from the repository."""
    def __init__(self, repository):
        self._repository = repository

    def execute(self, document_checksum: str):
        return self._repository.delete(document_checksum)