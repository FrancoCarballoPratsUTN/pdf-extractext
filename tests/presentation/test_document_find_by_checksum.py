import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.dependencies.dependencies import get_find_document_use_case
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError

client = TestClient(app)

def test_find_document_success(mock_document_success):

    checksum = "UNIQUE-FILE-CODE"

    app.dependency_overrides[get_find_document_use_case] = lambda: mock_document_success

    response = client.get(f"/find/{checksum}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["checksum"] == checksum
    assert "text" in data
    assert "file_name" in data


def test_find_document_not_found(mock_document_error):

    error_instance = mock_document_error(DocumentNotFoundError("Document not found"))
    
    app.dependency_overrides[get_find_document_use_case] = lambda: error_instance

    response = client.get("/find/NO-EXIST-CODE")

    assert response.status_code == 404
    assert response.json()["detail"] == "Document not found"