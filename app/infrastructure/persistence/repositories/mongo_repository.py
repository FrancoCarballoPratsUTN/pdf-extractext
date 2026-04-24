from dataclasses import asdict
from pymongo import ReturnDocument
from app.infrastructure.persistence.database.connection import get_collection
from app.domain.repositories.document_repository import DocumentRepository
from app.infrastructure.persistence.repositories.to_dto import to_document_dto
from app.domain.entities.document import Document

class MongoRepository(DocumentRepository):
    """MongoDB implementation of the DocumentRepository interface."""
    def __init__(self):
        self.collection = get_collection()

    def save(self, document: Document)-> Document:
        """Saves a document to the MongoDB collection.
        Args:
            document (Document): The document to be saved.
        Returns:            
            Document: The saved document.
        """
        dict_document = asdict(document)
        self.collection.insert_one(dict_document)
        return document

    def find_by_checksum(self, document_checksum: str)-> Document:
        """Finds a document by its checksum.
        Args:
            document_checksum (str): The checksum of the document to find.
        Returns:
            Document or None: The found document or None if not found.
        """
        document = self.collection.find_one({"checksum": document_checksum})

        return to_document_dto(document) if document else None

    def update(self, document_checksum: str, new_data: dict)-> Document:
        """Updates an existing document in the MongoDB collection.
        Args:
            document_checksum (str): The checksum of the document to update.
            new_data (dict): The new data to update the document with.
        Returns:
            Document or None: The updated document or None if not found.
        """
        updated_data = self.collection.find_one_and_update({"checksum": document_checksum},
                                                            {"$set": new_data},
                                                            return_document=ReturnDocument.AFTER)
        
        return to_document_dto(updated_data) if updated_data else None

    def delete(self, document_checksum: str)->dict:
        """Deletes a document from the MongoDB collection.
        Args:
            document_checksum (str): The checksum of the document to delete.
        Returns:
            dict: A message indicating the result of the delete operation.
        """
        self.collection.delete_one({"checksum": document_checksum})
        return {"message": "Document deleted successfully."}