from pydantic import BaseModel, Field

class DocumentUpload(BaseModel):
    file_name: str = Field(..., description="File name")
    file_type: str = Field(..., description="File type")
    file_size: int = Field(..., gt=0, le=15728640)
    file_content: bytes = Field(...)