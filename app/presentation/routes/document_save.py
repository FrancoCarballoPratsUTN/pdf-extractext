from app.presentation.schemas.exception_response import ProblemDetailsSchema
from fastapi import APIRouter, Depends, status
from app.presentation.schemas.document import DocumentSchema
from app.domain.entities.document import Document
from app.domain.exceptions.domain_exceptions import DocumentAlreadyExistsError, DocumentValidationError
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase
from app.infrastructure.dependencies.dependencies import get_save_document_use_case

router = APIRouter()

@router.post(
    '/save', 
    response_model=DocumentSchema, 
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {"model": ProblemDetailsSchema, "description": "Document already exists (Conflict)"},
        422: {"model": ProblemDetailsSchema, "description": "Validation error in business rules"}
    }
)
async def save_document(document: DocumentSchema, use_case: SaveDocumentUseCase = Depends(get_save_document_use_case)) -> DocumentSchema:
    """
    Args:
        document (DocumentSchema): Data from the document to be saved, received in the request body. This schema validates the input structure.
        use_case (SaveDocumentUseCase): Use case responsible for persisting the document in the system.

    Returns:
        DocumentSchema: The saved document.

    Raises:
        DocumentAlreadyExistsError: If a document with the same checksum is already registered (Handled as 409 Conflict).
        DocumentValidationError: If the provided data fails business rule validation (Handled as 422 Unprocessable Entity).
    """
    document_dataclass = Document(**document.model_dump())
    return use_case.execute(document_dataclass)