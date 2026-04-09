from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    """"
    Endpoint to upload a PDF file for text extraction.
    Args:        file (UploadFile): The PDF file to be uploaded.
    Returns:        dict: A dictionary containing the filename and a success message.
    """
    return {"filename": file.filename, "message": "File uploaded successfully"}