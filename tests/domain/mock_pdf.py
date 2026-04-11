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