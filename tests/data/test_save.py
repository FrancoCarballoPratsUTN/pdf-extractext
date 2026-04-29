from app.domain.exceptions.domain_exceptions import DocumentAlreadyExistsError
import pytest
from tests.conftest  import mock_document
from tests.data.mock_repository import get_mock_repository

def test_create_document(mock_document):
    """Test the save functionality of the MongoRepository."""
    mock_repo = get_mock_repository()
    new_document = mock_repo.save(mock_document)
    assert new_document is not None
    assert new_document.checksum == mock_document.checksum

def test_create_duplicate_document(mock_document):
    """Test saving a document with a duplicate checksum."""
    mock_repo = get_mock_repository()
    mock_repo.save(mock_document)

    with pytest.raises(DocumentAlreadyExistsError):
        mock_repo.save(mock_document)
    