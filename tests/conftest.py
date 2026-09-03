from datetime import datetime
from unittest.mock import MagicMock

import pytest

from app.domain.entities.document import Document
from app.main import app


@pytest.fixture
def mock_document():
    return Document(
        checksum="a6a6a6f6a6cv34",
        file_name="Test Document",
        text="This is a test document.",
        date=datetime(2026, 4, 27, 0, 0, 0),
    )


@pytest.fixture(autouse=True)
def clean_dependencies():
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def mock_document_success(mock_document):
    mock = MagicMock()

    def _execute(checksum=None, data=None, **kwargs):
        chk = (
            checksum.checksum
            if hasattr(checksum, "checksum")
            else (checksum or mock_document.checksum)
        )
        file_name = (
            data.get("file_name") if isinstance(data, dict) else None
        ) or mock_document.file_name
        text = (
            data.get("text") if isinstance(data, dict) else None
        ) or mock_document.text

        return {
            "file_name": file_name,
            "checksum": chk,
            "text": text,
            "date": "2026-04-27T00:00:00",
        }

    mock.execute.side_effect = _execute
    return mock


@pytest.fixture
def mock_document_error():
    def _generate(exception_to_raise):
        mock = MagicMock()
        mock.execute.side_effect = exception_to_raise
        return mock

    return _generate


@pytest.fixture
def file_upload(mock_document):
    return {
        "file": (
            mock_document.file_name,
            mock_document.text.encode("utf-8"),
            "application/pdf",
        )
    }
