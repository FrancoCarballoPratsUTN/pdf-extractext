import pytest
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from tests.conftest import mock_document
from tests.data.mock_repository import get_mock_repository

def test_find_by_checksum(mock_document):
    """Test the find_by_checksum functionality of the MongoRepository."""
    mock_repo = get_mock_repository()
    mock_repo.save(mock_document)

    found_document = mock_repo.find_by_checksum("a6a6a6f6a6cv34")
    assert found_document is not None
    assert found_document.checksum == mock_document.checksum

def test_find_by_checksum_not_found():
    """Test finding a document by checksum that does not exist."""
    mock_repo = get_mock_repository()
    with pytest.raises(DocumentNotFoundError):
        mock_repo.find_by_checksum("nonexistent_checksum")
        