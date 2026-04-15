from app.domain.use_cases.verifications.file_signature_validator import validate_pdf_signature

def test_validate_pdf_signature_success():
    file_content=b"%PDF-1.4\n%\xE2\xE3"

    assert validate_pdf_signature(file_content) == True

def test_validate_pdf_signature_fails():
    file_content=b"MZ\x90\x00\x03" 

    assert validate_pdf_signature(file_content) == False