from pypdf import PdfReader
import io

def liveness_check(document_content: bytes) -> bool:
    """
    Check if the PDF document is a valid PDF and can be read.
    
    Args:
        document_content (bytes): The content of the PDF document as bytes.

    Returns:
        bool: True if the PDF is valid and can be read, False otherwise.
    """
    try:
        
        reader = PdfReader(io.BytesIO(document_content))
        _ = reader.pages[0]
        return True

    except Exception as e:

        print(f"Integrity Error reading PDF: {e}")
        return False