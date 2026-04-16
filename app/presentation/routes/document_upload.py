from fastapi import HTTPException
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.domain.use_cases.flow_validation import do_validation
from app.presentation.middleware.check_middleware import check_middleware
from app.infrastructure.converters.extract_text import ExtractText
from fastapi import APIRouter, UploadFile, Depends


router = APIRouter()

@router.post('/upload')
async def upload_file(file_validate: UploadFile = Depends(check_middleware))-> str:
    """"
    Endpoint to upload a PDF file for text extraction.
    Args:        file (UploadFile): The PDF file to be uploaded.
    Returns:     str: file parse to text.
    """
    converter = ExtractText()
    await file_validate.seek(0)
    file_content = await file_validate.read()
    
    if not do_validation(file_content): 
        raise HTTPException(status_code= 400, detail= "Invalid PDF")

    conversor = ProcessDocumentUseCase(converter)
    text = conversor.execute(file_content)

    return text


    