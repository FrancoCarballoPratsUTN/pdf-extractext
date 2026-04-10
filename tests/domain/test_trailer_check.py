import pytest
from app.domain.use_cases.verifications.trailer_check import trailer_check
from app.domain.entities.document import Document

@pytest.fixture
def valid_pdf_document():
    """Fixture that provides a valid PDF document for testing."""
    return Document(
        file_name="valid.pdf",
        file_type="application/pdf",
        file_size=1024,
        file_content=b"%PDF-1.4\n%...\n%%EOF"
    )

@pytest.fixture
def invalid_pdf_document():
    """Fixture that provides an invalid PDF document for testing."""

    return Document(
        file_name="invalid.pdf",
        file_type="application/pdf",
        file_size=1024,
        file_content=b"%PDF-1.4\n%...\n"
    )

def test_trailer_check_valid(valid_pdf_document):
    """Test that the trailer_check function returns True for a valid PDF document."""
    assert trailer_check(valid_pdf_document) == True

def test_trailer_check_invalid(invalid_pdf_document):
    """Test that the trailer_check function returns False for an invalid PDF document."""
    assert trailer_check(invalid_pdf_document) == False