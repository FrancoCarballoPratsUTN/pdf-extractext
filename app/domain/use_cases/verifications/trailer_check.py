from app.domain.entities.document import Document

def trailer_check(document: Document) -> bool:
    """
    Verifies that the PDF document has a valid trailer.
    
    Args:
        document (Document): The PDF document to be checked.

    Returns:
        bool: True if the trailer is valid, False otherwise.

    """
    return document.file_content.endswith(b'%%EOF')