MAX_FILE_SIZE_BYTES = 15728640 
MIN_FILE_SIZE_BYTES = 0

def validate_file_size(file_size: float) -> bool:
    """
    Checks if a file size is within the allowed limits.

    Args:
        file_size (float): The size of the file in bytes to be validated.

    Returns:
        bool: True if the size is greater than 0 and less than 15MB, False otherwise.
    """
    return MIN_FILE_SIZE_BYTES < file_size < MAX_FILE_SIZE_BYTES
