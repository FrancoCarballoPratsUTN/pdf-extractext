import pytest
from app.domain.entities.document import Document
from app.domain.use_cases.verifications.file_size_validator import validate_file_size, MAX_FILE_SIZE_BYTES

def test_validate_file_size_success():
    document = Document(
        file_name="normal.pdf",
        file_type="application/pdf",
        file_size=1024,
        file_content=b"%PDF-"
    )

    validate_file_size(document)

def test_validate_file_size_fails_when_empty():
    document = Document(
        file_name="vacio.pdf",
        file_type="application/pdf",
        file_size=0,
        file_content=b""
    )

    with pytest.raises(ValueError, match="The file is empty."):
        validate_file_size(document)

def test_validate_file_size_fails_when_exceeds_limit():
    document = Document(
        file_name="pesado.pdf",
        file_type="application/pdf",
        file_size=MAX_FILE_SIZE_BYTES + 1,
        file_content=b"%PDF-")

    with pytest.raises(ValueError, match="The file exceeds the maximum allowed size of 15MB."):
        validate_file_size(document)