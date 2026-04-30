from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, file_content: bytes) -> bytes:
        """Converts the document content to a specific format."""
        pass