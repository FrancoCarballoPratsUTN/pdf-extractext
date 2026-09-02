from app.domain.use_cases.verifications.open_pdf import open_pdf


def file_has_only_images(pdf_content: bytes) -> bool:
    """
    Checks if the PDF is an image
    Returns True if NO extractable text is found.
    Returns False if the file contains text.
    """
    reader = open_pdf(pdf_content)

    for page in reader.pages:
        if page.extract_text():
            return False
    return True
