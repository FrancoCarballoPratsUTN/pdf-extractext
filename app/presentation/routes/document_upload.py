from app.domain.exceptions.domain_exceptions import DocumentValidationError
from app.infrastructure.dependencies.dependencies import get_process_document_use_case
from fastapi import HTTPException
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.presentation.middleware.check_middleware import check_middleware
from fastapi import APIRouter, UploadFile, Depends
from app.presentation.schemas.document import Document


router = APIRouter()

@router.post('/upload', response_model=Document)
async def upload_file(file_validate: UploadFile = Depends(check_middleware),
                      conversor: ProcessDocumentUseCase = Depends(get_process_document_use_case)  
                      )-> Document:
    """Endpoint to upload a PDF file for text extraction.
    Args:
        file (UploadFile): The PDF file to be uploaded.
    Returns:
        Document: The generated document entity only with the extracted text.
    """
    file_content = await file_validate.read()

    try:
        document_generated = conversor.execute(file_content, file_validate.filename)
        return document_generated

    except DocumentValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the document.")
    


    