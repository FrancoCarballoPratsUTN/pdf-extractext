def type_check(file_type: str) -> bool:
    """
    Checks if the provided file type is a valid PDF.
    Args:
        file_type (str): The MIME type of the file to be checked.
    Returns:
        bool: True if the file type is not a valid PDF, False otherwise.
    """
    return file_type == "application/pdf"