from dataclasses import dataclass

@dataclass
class Document:
    file_name: str 
    file_type: str 
    file_size: int 
    file_content: bytes
