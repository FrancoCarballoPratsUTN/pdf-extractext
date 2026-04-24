from dataclasses import asdict
from tests.conftest import mock_document
from tests.data.mock_repository import get_mock_repository

def test_find_by_checksum(mock_document):
    """Test the find_by_checksum functionality of the MongoRepository."""
    mock_repo = get_mock_repository()
    dict_document = asdict(mock_document)
    mock_repo.collection.insert_one(dict_document)

    found_document = mock_repo.find_by_checksum("a6a6a6f6a6cv34")
    assert found_document is not None
    assert found_document.checksum == mock_document.checksum