from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.dependencies.dependencies import get_update_document_use_case
from fastapi import Depends
from app.presentation.schemas.document import Document
from fastapi import HTTPException
from fastapi import APIRouter
from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase

router = APIRouter()
@router.put('/update/{checksum}', response_model=Document)
async def update_document(checksum: str, 
                          new_data: dict,
                          use_case: UpdateDocumentUseCase = Depends(get_update_document_use_case)
                          ) -> Document:
    """Endpoint to update a document.
    Args:
        checksum (str): The checksum of the document to be updated.
        new_data (dict): The new data to update the document with.
    Returns:
        Document: The updated document or a message if not found.
    """
    try:    
        updated_document = use_case.execute(checksum, new_data)
        return updated_document
    
    except DocumentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
