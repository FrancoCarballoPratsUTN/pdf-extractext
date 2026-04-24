from app.domain.use_cases.checksum import generate_checksum
from datetime import datetime
from app.domain.entities.document import Document

def flow_building(text: bytes, filename: str) -> Document:
    """Builds a document flow by creating a Document entity with the provided text and filename.
    Args:
        text (bytes): The content of the document in bytes.
        filename (str): The name of the file.
    Returns:
        Document: A Document entity containing the checksum, filename, and creation date.
    """
    checksum = generate_checksum(text)
    date_now = datetime.utcnow()
    
    document = Document(
        checksum=checksum,
        file_name=filename,
        text=text.decode('utf-8'),
        date=date_now
    )
    
    return document
    

