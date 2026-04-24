from fastapi import HTTPException
from fastapi import APIRouter
from app.presentation.schemas.document import Document
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase

rounter = APIRouter()

@rounter.post('/save')
async def save_document(document: Document) -> Document:
    """Endpoint to save a document.
    Args:
        document (Document): The document to be saved.
    Returns:
        Document: The saved document.
    """
    use_case = SaveDocumentUseCase()
    
    try:
        return use_case.execute(document)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))