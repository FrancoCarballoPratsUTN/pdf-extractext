import pytest
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from tests.conftest  import mock_document
from tests.data.mock_repository import get_mock_repository

def test_update_document(mock_document):
    """Test the update functionality of the MongoRepository."""
    collection = get_mock_repository()
    collection.save(mock_document)
    new_data = {"text": "Updated text content."}
    updated_document = collection.update(mock_document.checksum, new_data)
    assert updated_document is not None
    assert updated_document.text == "Updated text content."

def test_update_nonexistent_document(mock_document):
    """Test updating a non-existent document."""
    collection = get_mock_repository()
    new_data = {"text": "Updated text content."}
    
    with pytest.raises(DocumentNotFoundError):
        collection.update("nonexistent_checksum", new_data)
