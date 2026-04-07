from uuid import UUID

from app.domain.entities.document import Document
from app.domain.repositories.document_repository import DocumentRepository


class CreateDocumentUseCase:
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    async def execute(self, name: str, content: str) -> Document:
        document = Document.create(name=name, content=content)
        return await self._repository.create(document)


class GetDocumentUseCase:
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    async def execute(self, document_id: UUID) -> Document | None:
        return await self._repository.get_by_id(document_id)


class GetAllDocumentsUseCase:
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    async def execute(self) -> list[Document]:
        return await self._repository.get_all()


class DeleteDocumentUseCase:
    def __init__(self, repository: DocumentRepository):
        self._repository = repository

    async def execute(self, document_id: UUID) -> bool:
        return await self._repository.delete(document_id)
