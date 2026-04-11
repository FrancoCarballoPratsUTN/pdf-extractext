from app.domain.use_cases.verifications.encryptation_check import encryptation_check
from pypdf import PdfWriter
import io

def create_mock_pdf(encrypted: bool, password: str = "123456") -> bytes:
    """Helper function to create a mock PDF content."""
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)

    if encrypted:
        writer.encrypt(password)
    
    pdf_bytes = io.BytesIO()
    writer.write(pdf_bytes)

    return pdf_bytes.getvalue()

def test_encryptation_check_encrypted():
    """Test that the encryptation_check function returns True for an encrypted PDF."""
    encrypted_pdf = create_mock_pdf(encrypted=True)
    assert encryptation_check(encrypted_pdf) == True

def test_encryptation_check_not_encrypted():
    """Test that the encryptation_check function returns False for a non-encrypted PDF."""
    not_encrypted_pdf = create_mock_pdf(encrypted=False)
    assert encryptation_check(not_encrypted_pdf) == False

