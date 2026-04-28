from app.domain.entities.document import Document
from app.main import app
from datetime import datetime
from app.infrastructure.dependencies.dependencies import get_process_document_use_case
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


@pytest.fixture(autouse=True)
def clean_dependencies():
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def override(monkeypatch, mock_document):
    class MockUseCase:
        def execute(self, file_name, text):
            return mock_document["result"]
        
    app.dependency_overrides[get_process_document_use_case] = lambda: MockUseCase()
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def mock_document_success(mock_document):
    class UniversalMock:
        def __init__(self, original_dto):
            self.file_name = original_dto.file_name
            self.text = original_dto.text
            self.checksum = original_dto.checksum
            self.date = original_dto.date

        def execute(self, checksum=None, data=None, **kwargs):
            """Allows dynamic response based on input, useful for multiple test scenarios."""
     
            current_checksum = checksum
            try:
                current_checksum = checksum.checksum
            except AttributeError:
                current_checksum = checksum
            
            final_text = self.text
            if data and isinstance(data, dict) and "text" in data:
                final_text = data["text"]
            elif hasattr(checksum, "text"):
                final_text = checksum.text

            return {
                "file_name": self.file_name,
                "checksum": current_checksum or self.checksum,
                "text": final_text,
                "date": "2026-04-27T00:00:00"
            }

    return UniversalMock(mock_document)

@pytest.fixture
def mock_document_error():
    def _generate_error(exception_to_raise):
        class ErrorMock:
            def execute(self, *args, **kwargs):
                raise exception_to_raise
        return ErrorMock()
    return _generate_error

@pytest.fixture
def file_upload(mock_document):
    file_upload = {
        "file": (
            mock_document.file_name,
            mock_document.text.encode("utf-8"),
            "application/pdf"
        )
    }
    return file_upload