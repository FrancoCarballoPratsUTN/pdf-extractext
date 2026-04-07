from dataclasses import dataclass
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.data.database.connection import get_database
from app.data.repositories.document_repository import MongoDocumentRepository
from app.domain.use_cases import (
    CreateDocumentUseCase,
    DeleteDocumentUseCase,
    GetAllDocumentsUseCase,
    GetDocumentUseCase,
)
from app.presentation.schemas.document import DocumentCreate, DocumentResponse


@dataclass
class DocumentUseCases:
    create: CreateDocumentUseCase
    get: GetDocumentUseCase
    get_all: GetAllDocumentsUseCase
    delete: DeleteDocumentUseCase


router = APIRouter(prefix="/documents", tags=["documents"])


def get_document_use_cases(
    db: AsyncIOMotorDatabase = Depends(get_database),
) -> DocumentUseCases:
    repository = MongoDocumentRepository(db)
    return DocumentUseCases(
        create=CreateDocumentUseCase(repository),
        get=GetDocumentUseCase(repository),
        get_all=GetAllDocumentsUseCase(repository),
        delete=DeleteDocumentUseCase(repository),
    )


@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def create_document(
    document_data: DocumentCreate,
    use_cases: DocumentUseCases = Depends(get_document_use_cases),
):
    document = await use_cases.create.execute(
        name=document_data.name,
        content=document_data.content,
    )
    return document


@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(
    document_id: UUID,
    use_cases: DocumentUseCases = Depends(get_document_use_cases),
):
    document = await use_cases.get.execute(document_id)
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return document


@router.get("/", response_model=list[DocumentResponse])
async def get_all_documents(
    use_cases: DocumentUseCases = Depends(get_document_use_cases),
):
    documents = await use_cases.get_all.execute()
    return documents


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(
    document_id: UUID,
    use_cases: DocumentUseCases = Depends(get_document_use_cases),
):
    deleted = await use_cases.delete.execute(document_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return None
