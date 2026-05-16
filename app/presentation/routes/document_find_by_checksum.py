from app.presentation.schemas.exception_response import ProblemDetailsSchema
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from fastapi import Depends
from app.infrastructure.dependencies.dependencies import get_find_document_use_case
from app.presentation.schemas.document import DocumentSchema
from fastapi import APIRouter
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase

router = APIRouter()
@router.get(
    '/find/{checksum}', 
    response_model=DocumentSchema,
    responses={
        404: {"model": ProblemDetailsSchema, "description": "Document not found by the provided checksum"},
        500: {"model": ProblemDetailsSchema, "description": "Internal server error during document retrieval"}
    }
)
async def find_document_by_checksum(checksum: str,use_case: FindDocumentUseCase = Depends(get_find_document_use_case)) -> DocumentSchema:
    """
    Args:
        checksum (str): Unique identifier of the document to search for.
        use_case (FindDocumentUseCase): Use case responsible for searching and returning the document.

    Returns:
        DocumentSchema: Found document that matches the provided checksum.

    Raises: DocumentNotFoundError: If no document matches the provided checksum (Handled globally as 404).
    """
    return use_case.execute(checksum)