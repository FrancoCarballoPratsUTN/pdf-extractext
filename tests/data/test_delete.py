from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
import pytest
from tests.data.mock_repository import get_mock_repository
from tests.conftest import mock_document

def test_delete_document(mock_document):
    """Test the delete functionality of the MongoRepository."""
    
    collection = get_mock_repository()
    collection.save(mock_document)
    response = collection.delete(mock_document.checksum)
    assert response == {"message": "Document deleted successfully."}

def test_delete_nonexistent_document():
    """Test deleting a non-existent document."""
    collection = get_mock_repository()
    with pytest.raises(DocumentNotFoundError, match="Document with checksum nonexistent_checksum not found."):
        collection.delete("nonexistent_checksum")

    