from datetime import datetime
from pydantic import BaseModel, Field

class Document(BaseModel):
    file_name: str = Field(..., description="File name")
    checksum: str = Field(..., description="Checksum of the document")
    text: str = Field(..., description="Extracted text")
    date: datetime = Field(...)