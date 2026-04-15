from fastapi import HTTPException
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.infrastructure.converters.docling_md import DoclingConverterMd
from app.domain.use_cases.pipeline import do_validation
from app.presentation.middleware.check_middleware import check_middleware
from fastapi import APIRouter, UploadFile, Depends


router = APIRouter()

@router.post('/upload')
async def upload_file(file_validate: UploadFile = Depends(check_middleware))-> str:
    """"
    Endpoint to upload a PDF file for text extraction.
    Args:        file (UploadFile): The PDF file to be uploaded.
    Returns:     str: file parse to markdown.
    """
    converter = DoclingConverterMd()
    await file_validate.seek(0)
    file_content = await file_validate.read()
    file_name = file_validate.filename

    if not do_validation(file_content): 
        raise HTTPException(status_code= 400, detail= "Invalid PDF")

    conversor = ProcessDocumentUseCase(converter)
    markdown = conversor.execute(file_content, file_name)

    return markdown


    