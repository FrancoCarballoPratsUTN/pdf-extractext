import io

from pypdf import PdfReader


def open_pdf(content: bytes) -> PdfReader:
    """Opens a PDF from raw bytes and returns a PdfReader instance."""
    return PdfReader(io.BytesIO(content))
