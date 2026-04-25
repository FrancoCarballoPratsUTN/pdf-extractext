from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
class UpdateDocumentUseCase:
    """Use case for updating a document in the repository."""
    def __init__(self, repository):
        self._repository = repository

    def execute(self, document_checksum: str, updated_data: dict):
        updated_document = self._repository.update(document_checksum, updated_data)
        return updated_document