from dataclasses import dataclass
from datetime import datetime


@dataclass
class Document:
    file_name: str
    checksum: str
    text: str
    date: datetime
