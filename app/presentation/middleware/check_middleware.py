from fastapi import UploadFile, HTTPException, File
from app.domain.use_cases.verifications.file_size_validator import validate_file_size
from app.domain.use_cases.verifications.type_check import type_check

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
        raise HTTPException(status_code= 400, detail= "Invalid File")

    if not validate_file_size(file_size=file_size):
        raise HTTPException( status_code= 400, detail= "the file size is not within the limite")
    
    return file

    