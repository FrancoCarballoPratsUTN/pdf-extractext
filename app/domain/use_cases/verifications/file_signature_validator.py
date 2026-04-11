from app.domain.entities.document import Document

pdf_magic_number = b"%PDF-"

def validate_pdf_signature(document: Document) -> None:

    if not document.file_content.startswith(pdf_magic_number):
        raise ValueError("The file is not a valid PDF")