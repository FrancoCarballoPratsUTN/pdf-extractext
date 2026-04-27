from app.presentation.schemas.document import Document_Schema
def to_document_dto(document: dict) -> Document_Schema:
    """Converts a dictionary document to a Document DTO.
    Args:        document (dict): The dictionary document to convert.
    Returns:        Document: The converted Document DTO.
    """
    return Document_Schema(
        file_name=document.get("file_name"),
        checksum=document.get("checksum"),
        text=document.get("text"),
        date=document.get("date")
    )