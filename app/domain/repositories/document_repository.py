from abc import ABC, abstractmethod

class DocumentRepository(ABC):
    """Interface for document repository."""
    @abstractmethod
    def save(self, document):
        pass

    @abstractmethod
    def find_by_checksum(self, document_checksum):
        pass

    @abstractmethod
    def update(self, document_checksum, new_data):
        pass

    @abstractmethod
    def delete(self, document_checksum):
        pass

    