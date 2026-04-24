from app.domain.entities.document import Document
from datetime import datetime
import pytest

@pytest.fixture
def mock_document():
    """Fixture that provides a mock Document instance for testing."""
    document = Document(
        checksum="a6a6a6f6a6cv34",
        file_name="Test Document",
        text="This is a test document.",
        date=datetime.now()
    )
    return document