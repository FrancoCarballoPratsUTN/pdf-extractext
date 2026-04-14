from app.domain.entities.document import Document

PDF_MAGIC_NUMBER = b"%PDF-"

def validate_pdf_signature(document: Document) -> bool:

    """Validates that the provided document has a valid PDF signature

    Args:
        document(Document): The document to be validated
    Returns:
        bool: True if the document has a valid PDF signature, False otherwise
    """

    return document.file_content.startswith(PDF_MAGIC_NUMBER)