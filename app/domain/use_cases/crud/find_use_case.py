
class FindDocumentUseCase:
    """Use case for finding a document in the repository."""
    def __init__(self, repository):
        self._repository = repository

    def execute(self, document_checksum: str):
        return self._repository.find_by_checksum(document_checksum)