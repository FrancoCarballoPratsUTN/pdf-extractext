from datetime import datetime
from dataclasses import dataclass

@dataclass
class Document:
    file_name: str 
    checksum: str 
    text: str 
    date: datetime
