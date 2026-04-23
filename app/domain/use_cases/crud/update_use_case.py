from app.infrastructure.persistence.document_repository import DocumentRepository

class UpdateDocumentUseCase:

    def __init__(self, repository: DocumentRepository):
        pass
    
    def execute(self, document_id, updated_data):
        pass