import pytest
from app.domain.entities.document import Document
from app.domain.use_cases.verifications.file_signature_validator import validate_pdf_signature

def test_validate_pdf_signature_success():
    document = Document(
        file_name="valido.pdf",
        file_type="application/pdf",
        file_size=1024,
        file_content=b"%PDF-1.4\n%\xE2\xE3"
    )
    
    validate_pdf_signature(document)

def test_validate_pdf_signature_fails():
    document = Document(
        file_name="falso.pdf",
        file_type="application/pdf",
        file_size=1024,
        file_content=b"MZ\x90\x00\x03" 
    )
    
    with pytest.raises(ValueError, match="The file is not a valid PDF"):
        validate_pdf_signature(document)