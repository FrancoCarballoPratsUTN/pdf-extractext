from app.domain.exceptions.domain_exceptions import DocumentAlreadyExistsError
from app.infrastructure.dependencies.dependencies import get_save_document_use_case
from fastapi import Depends
from fastapi import HTTPException
from fastapi import APIRouter
from app.presentation.schemas.document import Document_Schema
from app.domain.entities.document import Document
from app.domain.use_cases.crud.save_use_case import SaveDocumentUseCase

router = APIRouter()

@router.post('/save')
async def save_document(document: Document_Schema,
                        use_case: SaveDocumentUseCase = Depends(get_save_document_use_case)
                        ) -> Document_Schema:
    """Endpoint to save a document.
    Args:
        document (Document): The document to be saved.
    Returns:
        Document: The saved document.
    """
    document_dataclass = Document(**document.model_dump())
    try:
        return use_case.execute(document_dataclass)

    except DocumentAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))