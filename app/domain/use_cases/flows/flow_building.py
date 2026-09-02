from datetime import UTC, datetime

from app.domain.entities.document import Document
from app.domain.use_cases.checksum import generate_checksum


def flow_building(text: str, filename: str) -> Document:
    """Builds a document flow creating a Document with the text and filename.
    Args:
        text (str): The content of the document.
        filename (str): The name of the file.
    Returns:
        Document: Document entity with checksum, filename, and creation date.
    """
    checksum = generate_checksum(text.encode("utf-8"))
    date_now = datetime.now(UTC)

    document = Document(
        checksum=checksum, file_name=filename, text=text, date=date_now
    )

    return document
