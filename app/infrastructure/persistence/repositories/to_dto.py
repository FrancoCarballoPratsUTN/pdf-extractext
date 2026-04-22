from app.presentation.schemas.document import Document
def to_document_dto(document: dict) -> Document:
    """Converts a MongoDB document to a Document DTO.
    Args:        document (dict): The MongoDB document to convert.
    Returns:        Document: The converted Document DTO.
    """
    return Document(
        file_name=document.get("file_name"),
        checksum=document.get("checksum"),
        text=document.get("text"),
        date=document.get("date")
    )