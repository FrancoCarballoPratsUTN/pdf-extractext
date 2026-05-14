from fastapi import APIRouter, Depends, status
from app.presentation.schemas.document import Document_Schema
from app.domain.entities.document import Document
from app.domain.exceptions.domain_exceptions import DocumentAlreadyExistsError, DocumentValidationError
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase
from app.infrastructure.dependencies.dependencies import get_save_document_use_case

router = APIRouter()

@router.post(
    '/save', 
    response_model=Document_Schema, 
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {"description": "Document already exists (Conflict)"},
        422: {"description": "Validation error in business rules"}
    }
)
async def save_document(document: Document_Schema, use_case: SaveDocumentUseCase = Depends(get_save_document_use_case)) -> Document_Schema:
    """
    Args:
        document (Document_Schema): Data from the document to be saved, received in the request body. This schema validates the input structure.
        use_case (SaveDocumentUseCase): Use case responsible for persisting the document in the system.

    Returns:
        Document_Schema: The saved document.

    Raises:
        DocumentAlreadyExistsError: If a document with the same checksum is already registered (Handled as 409 Conflict).
        DocumentValidationError: If the provided data fails business rule validation (Handled as 422 Unprocessable Entity).
    """
    document_dataclass = Document(**document.model_dump())
    return use_case.execute(document_dataclass)