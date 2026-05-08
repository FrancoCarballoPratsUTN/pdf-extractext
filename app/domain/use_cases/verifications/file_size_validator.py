from app.config.settings import settings

MAX_FILE_SIZE_BYTES = settings.max_bytes 
MIN_FILE_SIZE_BYTES = settings.min_bytes 

def validate_file_size(file_size: float) -> bool:
    """
    Checks if a file size is within the allowed limits.

    Args:
        file_size (float): The size of the file in bytes to be validated.

    Returns:
        bool: True if the size is greater than 0 and less than 15MB, False otherwise.
    """
    return MIN_FILE_SIZE_BYTES < file_size < MAX_FILE_SIZE_BYTES
