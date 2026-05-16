from app.presentation.schemas.exception_response import ProblemDetailsSchema
from app.infrastructure.dependencies.dependencies import get_process_document_use_case
from app.domain.use_cases.converter import ProcessDocumentUseCase
from app.presentation.middleware.check_middleware import check_middleware
from fastapi import APIRouter, UploadFile, Depends, status
from app.presentation.schemas.document import DocumentSchema

router = APIRouter()

@router.post(
    '/upload', 
    response_model=DocumentSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        422: {"model": ProblemDetailsSchema, "description": "Document validation failed (corrupted or invalid structure)"},
        500: {"model": ProblemDetailsSchema, "description": "Internal error during text extraction or file processing"}
    }
)
async def upload_file(file_validate: UploadFile = Depends(check_middleware), conversor: ProcessDocumentUseCase = Depends(get_process_document_use_case)) -> DocumentSchema:
    """
    Endpoint to upload and process a file.
    Args:
        file_validate (UploadFile):
           File previously validated using the `check_middleware` middleware.
            Contains the file and metadata (`filename`).

        conversor (ProcessDocumentUseCase):
            Use case responsible for processing the file content
            and generating a document in the system.
    Returns:
        DocumentSchema:
            Representation of the processed and stored document.
    Raises:
        DocumentValidationError: If the file content violates domain rules or is corrupted (Handled globally as 422).
        DocumentProcessingError: If an unexpected error occurs during text conversion (Handled globally as 500).
    """
    file_content = await file_validate.read()
    document_generated = conversor.execute(file_content, file_validate.filename)
    return document_generated
    