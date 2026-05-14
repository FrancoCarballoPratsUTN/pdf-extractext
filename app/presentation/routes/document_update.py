from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.dependencies.dependencies import get_update_document_use_case
from fastapi import Depends, status
from app.presentation.schemas.document import Document_Schema
from fastapi import APIRouter
from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase

router = APIRouter()
@router.put(
    '/update/{checksum}', 
    response_model=Document_Schema,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"description": "Document not found by the provided checksum"},
        422: {"description": "Validation error in the update data"},
        500: {"description": "Internal server error during document update"}
    }
)
async def update_document(checksum: str, new_data: dict,use_case: UpdateDocumentUseCase = Depends(get_update_document_use_case)) -> Document_Schema:
    """
    Args:
        checksum (str): Unique identifier of the document to be updated.
        new_data (dict): Dictionary containing the new data to be updated in the document.
        use_case (UpdateDocumentUseCase): Use case responsible for applying the document update in the system.

    Returns:
        Document_Schema: Updated document after applying the changes.

    Raises:     
        DocumentNotFoundError: If the checksum does not match any record (Handled globally as 404).
        DocumentValidationError: If the new_data violates domain constraints (Handled globally as 422).
    """
    return use_case.execute(checksum, new_data)