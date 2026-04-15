from fastapi import HTTPException
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.infrastructure.converters.docling_md import DoclingConverterMd
from app.domain.use_cases.pipeline import do_validation
from app.presentation.middleware.check_middleware import check_middleware
from fastapi import APIRouter, UploadFile, Depends


router = APIRouter()

@router.post('/upload')
async def upload_file(file: UploadFile = Depends(check_middleware))-> str:
    """"
    Endpoint to upload a PDF file for text extraction.
    Args:        file (UploadFile): The PDF file to be uploaded.
    Returns:     str: file parse to markdown.
    """
    converter = DoclingConverterMd()
    file_content = await file.read()

    if do_validation(file_content): 
        raise HTTPException(status_code= 400, details= "Invalid PDF")

    conversor = ProcessDocumentUseCase(converter)
    markdown = conversor.execute(file_content)

    return markdown


    