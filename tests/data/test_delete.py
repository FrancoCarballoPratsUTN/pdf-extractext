from dataclasses import asdict
from tests.data.mock_repository import get_mock_repository
from tests.conftest import mock_document

def test_delete_document(mock_document):
    """Test the delete functionality of the MongoRepository."""
    
    collection = get_mock_repository()
    dict_document = asdict(mock_document)
    collection.collection.insert_one(dict_document)
    response = collection.delete(mock_document.checksum)
    assert response == {"message": "Document deleted successfully."}