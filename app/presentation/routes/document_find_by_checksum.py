from fastapi import HTTPException
from app.presentation.schemas.document import Document
from fastapi import APIRouter
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase

router = APIRouter()
@router.get('/find/{checksum}', response_model=Document)
async def find_document_by_checksum(checksum: str) -> Document:
    """Endpoint to find a document by its checksum.
    Args:
        checksum (str): The checksum of the document to be found.
    Returns:
        Document: The found document or a message if not found.
    """
    use_case = FindDocumentUseCase()

    try:
        document = use_case.execute(checksum)
        return document
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
