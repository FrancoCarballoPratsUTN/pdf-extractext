from app.domain.entities.document import Document

MAX_FILE_SIZE_BYTES = 15728640 

def validate_file_size(document: Document) -> None:

    if document.file_size == 0:
        raise ValueError("The file is empty.")

    if document.file_size > MAX_FILE_SIZE_BYTES:
        raise ValueError("The file exceeds the maximum allowed size of 15MB.")