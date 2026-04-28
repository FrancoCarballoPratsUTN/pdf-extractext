import pytest
from fastapi.testclient import TestClient
from app.infrastructure.dependencies.dependencies import get_process_document_use_case
from app.main import app

client = TestClient(app)

def test_upload_pdf_structure(mock_document, mock_document_success, file_upload):

    app.dependency_overrides[get_process_document_use_case] = ( lambda: mock_document_success )

    response = client.post("/upload", files=file_upload)

    assert response.status_code == 200
    assert response.json()["file_name"] == mock_document.file_name