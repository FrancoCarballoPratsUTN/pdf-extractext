from app.domain.exceptions.domain_exceptions import InvalidDocumentDataError
from fastapi import UploadFile, HTTPException, File
from app.domain.use_cases.verifications.file_size_validator import validate_file_size
from app.domain.use_cases.verifications.type_check import type_check
from app.config.logging_config import loger

def check_middleware(file: UploadFile =File(...))-> UploadFile:
    """
    Middleware to validate the uploaded file's type and size.
    Args:
        file (UploadFile): The uploaded file to be validated.   
    Returns:
        UploadFile: The validated uploaded file."""
    file_type = file.content_type 
    file_size = file.size

    if not type_check(file_type=file_type):
        loger.warning(f"Invalid file type: {file_type}. Only PDF files are allowed.")
        raise InvalidDocumentDataError("Invalid file type. Only PDF files are allowed.")

    if not validate_file_size(file_size=file_size):
        loger.warning(f"File size {file_size} bytes is not within the allowed limit.")
        raise InvalidDocumentDataError("the file size is not within the limite")
    
    loger.info(f"File {file.filename} passed validation checks. Type: {file_type}, Size: {file_size} bytes.")
    return file

    