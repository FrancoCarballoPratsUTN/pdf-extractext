from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from fastapi import Depends
from app.infrastructure.dependencies.dependencies import get_find_document_use_case
from fastapi import HTTPException
from app.presentation.schemas.document import Document_Schema
from fastapi import APIRouter
from app.domain.use_cases.crud.find_use_case import FindDocumentUseCase

router = APIRouter()
@router.get('/find/{checksum}', response_model=Document_Schema)
async def find_document_by_checksum(checksum: str,
                                    use_case: FindDocumentUseCase = Depends(get_find_document_use_case)
                                    ) -> Document_Schema:
    """Endpoint to find a document by its checksum.
    Args:
        checksum (str): The checksum of the document to be found.
    Returns:
        Document: The found document or a message if not found.
    """

    try:
        document = use_case.execute(checksum)
        return document
        
    except DocumentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
