from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.dependencies.dependencies import get_delete_document_use_case
from fastapi import Depends
from fastapi import HTTPException
from fastapi import APIRouter
from app.domain.use_cases.crud.delete_use_case import DeleteDocumentUseCase

router = APIRouter()
@router.delete('/delete/{checksum}')
async def delete_document(checksum: str,
                          use_case: DeleteDocumentUseCase = Depends(get_delete_document_use_case)
                          ) -> dict:
    """Endpoint to delete a document.
    Args:
        checksum (str): The checksum of the document to be deleted.
    Returns:
        dict: A message indicating the result of the delete operation.
    """


    try:
        return use_case.execute(checksum)

    except DocumentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))