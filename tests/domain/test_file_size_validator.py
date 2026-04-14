import pytest
from app.domain.entities.document import Document
from app.domain.use_cases.verifications.file_size_validator import validate_file_size, MAX_FILE_SIZE_BYTES

def test_validate_file_size_success():
    file_size = 1024
    validate_file_size(file_size)

def test_validate_file_size_fails_when_empty():
    file_size = 0
    validate_file_size(file_size)

def test_validate_file_size_fails_when_exceeds_limit():
    file_size = MAX_FILE_SIZE_BYTES + 1
    validate_file_size(file_size)