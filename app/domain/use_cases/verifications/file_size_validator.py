
def validate_file_size(file_size: float, file_min: float, file_max: float) -> bool:
    """
    Checks if a file size is within the allowed limits.

    Args:
        file_size (float): The size of the file in bytes to be validated.

    Returns:
        bool: True if the size is greater than 0 and less than 15MB, False otherwise.
    """
    return file_min < file_size < file_max
