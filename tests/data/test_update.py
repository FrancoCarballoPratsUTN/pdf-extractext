from dataclasses import asdict
from app.infrastructure.persistence.database.connection import collection
from tests.conftest  import mock_document
from tests.data.mock_repository import get_mock_repository

def test_update_document(mock_document):
    """Test the update functionality of the MongoRepository."""
    collection = get_mock_repository()
    dict_document = asdict(mock_document)
    collection.collection.insert_one(dict_document)
    new_data = {"text": "Updated text content."}
    updated_document = collection.update(mock_document.checksum, new_data)
    assert updated_document is not None
    assert updated_document.text == "Updated text content."
