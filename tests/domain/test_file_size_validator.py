from app.domain.use_cases.verifications.file_size_validator import validate_file_size, MAX_FILE_SIZE_BYTES

def test_validate_file_size_success():
    file_size = 1024
    assert validate_file_size(file_size) == True

def test_validate_file_size_fails_when_empty():
    file_size = 0
    assert validate_file_size(file_size) == False

def test_validate_file_size_fails_when_exceeds_limit():
    file_size = MAX_FILE_SIZE_BYTES + 1
    assert validate_file_size(file_size) == False