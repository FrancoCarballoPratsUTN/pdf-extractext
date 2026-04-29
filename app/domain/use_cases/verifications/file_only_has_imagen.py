from pypdf import PdfReader
import io

def file_has_imagen(pdf_content: bytes) -> bool:
    """
    Checks if the PDF is an image
    Returns True if NO extractable text is found.
    Returns False if the file contains text.
    """
    reader = PdfReader(io.BytesIO(pdf_content))
    accumulated_text = ""
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            accumulated_text += text       
    return len(accumulated_text.strip()) == 0