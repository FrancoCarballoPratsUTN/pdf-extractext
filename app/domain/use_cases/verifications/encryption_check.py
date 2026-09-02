import logging

from app.domain.use_cases.verifications.open_pdf import open_pdf

logger = logging.getLogger(__name__)


def encryption_check(document_content: bytes) -> bool:
    """
    Check if the PDF document is encrypted.
    Args:
        document_content (bytes): The content of the PDF document as bytes.
    Returns:
        bool: True if the PDF is encrypted, False otherwise.
    """
    try:
        reader = open_pdf(document_content)
        logger.info("PDF encryption check completed successfully.")
        return reader.is_encrypted

    except Exception as e:
        logger.warning(f"Error reading PDF: {e}", exc_info=True)
        return False
