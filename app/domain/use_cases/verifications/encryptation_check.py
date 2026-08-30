import io

from pypdf import PdfReader

from app.config.logging_config import loger


def encryptation_check(document_content: bytes) -> bool:
    """
    Check if the PDF document is encrypted.
    Args:
        document_content (bytes): The content of the PDF document as bytes.
    Returns:
        bool: True if the PDF is encrypted, False otherwise.
    """
    try:
        reader = PdfReader(io.BytesIO(document_content))
        loger.info("PDF encryption check completed successfully.")
        return reader.is_encrypted

    except Exception as e:
        loger.warning(f"Error reading PDF: {e}", exc_info=True)
        return False
