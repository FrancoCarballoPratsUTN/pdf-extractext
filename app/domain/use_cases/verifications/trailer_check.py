
def trailer_check(document_content: bytes) -> bool:
    """
    Verifies that the PDF document has a valid trailer.
    
    Args:
        document_content (bytes): The content of the PDF document as bytes.

    Returns:
        bool: True if the trailer is valid, False otherwise.

    """
    return document_content.endswith(b'%%EOF')