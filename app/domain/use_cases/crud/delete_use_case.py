from app.infrastructure.persistence.document_repository import DocumentRepository

class DeleteDocumentUseCase:

    def __init__(self, repository: DocumentRepository):
        pass

    def execute(self, document_id):
        pass