from pypdf import PdfReader
from pypdf import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_mock_pdf(encrypted: bool, password: str = "123456", is_image: bool = False) -> bytes:
    """Helper function to create a mock PDF content."""
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    if not is_image:
        can.setFont("Helvetica", 12)
        can.drawString(100, 680, "It is a test PDF document.")
    else:
        can.rect(100, 600, 400, 100, fill=0) 

    can.save()
    
    packet.seek(0)
    new_pdf = PdfReader(packet)
    writer = PdfWriter()
    writer.add_page(new_pdf.pages[0])

    if encrypted:
        writer.encrypt(password)
    
    final_buffer = io.BytesIO()
    writer.write(final_buffer)

    return final_buffer.getvalue()