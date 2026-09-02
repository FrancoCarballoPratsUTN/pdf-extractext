from fastapi import APIRouter, Depends, status

from app.domain.use_cases.crud.update_use_case import UpdateDocumentUseCase
from app.infrastructure.dependencies.dependencies import get_update_document_use_case
from app.presentation.schemas.document import DocumentSchema, UpdateDocumentSchema
from app.presentation.schemas.exception_response import ProblemDetailsSchema

router = APIRouter()


@router.put(
    "/update/{checksum}",
    response_model=DocumentSchema,
    status_code=status.HTTP_200_OK,
    responses={
        404: {
            "model": ProblemDetailsSchema,
            "description": "Document not found by the provided checksum",
        },
        422: {
            "model": ProblemDetailsSchema,
            "description": "Validation error in the update data",
        },
        500: {
            "model": ProblemDetailsSchema,
            "description": "Internal server error during document update",
        },
    },
)
async def update_document(
    checksum: str,
    new_data: UpdateDocumentSchema,
    use_case: UpdateDocumentUseCase = Depends(get_update_document_use_case),
) -> DocumentSchema:
    """
    Args:
        checksum (str): Unique identifier of the document to be updated.
        new_data (UpdateDocumentSchema): Schema with the new data for the document.
        use_case (UpdateDocumentUseCase): Use case that applies the document update.

    Returns:
        DocumentSchema: Updated document after applying the changes.

    Raises:
        DocumentNotFoundError: If the checksum does not match any record (404).
        DocumentValidationError: If the new_data violates domain constraints (422).
    """
    return use_case.execute(checksum, new_data.model_dump(exclude_none=True))
