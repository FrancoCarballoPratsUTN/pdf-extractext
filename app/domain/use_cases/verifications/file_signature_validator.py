PDF_MAGIC_NUMBER = b"%PDF-"

def validate_pdf_signature(file_content: bytes) -> bool:

    """Validates that the provided document has a valid PDF signature

    Args:
        file_content (bytes): The content of the file to be validated.
    Returns:
        bool: True if the file has a valid PDF signature, False otherwise
    """

    return file_content.startswith(PDF_MAGIC_NUMBER)