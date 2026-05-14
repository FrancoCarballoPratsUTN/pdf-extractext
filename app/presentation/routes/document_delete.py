from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.dependencies.dependencies import get_delete_document_use_case
from fastapi import Depends
from fastapi import APIRouter
from app.domain.use_cases.crud.delete_use_case import DeleteDocumentUseCase

router = APIRouter()
@router.delete('/delete/{checksum}', 
    response_model=dict,
    status_code=200,
    responses={
        404: {"description": "Document not found"},
        500: {"description": "Internal server error during deletion"}
    })
async def delete_document(checksum: str, use_case: DeleteDocumentUseCase = Depends(get_delete_document_use_case)) -> dict:
    """
    Args:
        checksum (str): The unique SHA-256 identifier of the document to be deleted.
        use_case (DeleteDocumentUseCase): Injected service that handles the deletion logic.

    Returns:
        dict: A confirmation message indicating the successful removal of the document.

    Raises:
        DocumentNotFoundError: If no document matches the provided checksum (404).
    """
    return use_case.execute(checksum)