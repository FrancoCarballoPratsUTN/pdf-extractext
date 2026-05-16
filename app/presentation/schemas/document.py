from pydantic import ConfigDict
from datetime import datetime
from pydantic import BaseModel, Field

class DocumentSchema(BaseModel):
    file_name: str = Field(..., description="File name")
    checksum: str = Field(..., description="Checksum of the document")
    text: str = Field(..., description="Extracted text")
    date: datetime = Field(...)
    model_config = ConfigDict(from_attributes=True)