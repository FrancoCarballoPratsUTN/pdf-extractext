
from app.config.settings import settings
from app.domain.use_cases.verifications.file_size_validator import validate_file_size

MIN_FILE_SIZE_BYTES = settings.min_bytes
MAX_FILE_SIZE_BYTES = settings.max_bytes

def test_validate_file_size_success():
    file_size = 1024
    assert validate_file_size(file_size, MIN_FILE_SIZE_BYTES, MAX_FILE_SIZE_BYTES)


def test_validate_file_size_fails_when_empty():
    file_size = 0
    assert not validate_file_size(file_size, MIN_FILE_SIZE_BYTES, MAX_FILE_SIZE_BYTES)


def test_validate_file_size_fails_when_exceeds_limit():
    file_size = MAX_FILE_SIZE_BYTES + 1
    assert not validate_file_size(file_size, MIN_FILE_SIZE_BYTES, MAX_FILE_SIZE_BYTES)
