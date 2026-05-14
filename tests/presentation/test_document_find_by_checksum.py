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
    checksum = "NO-EXIST-CODE"

    error_message = "Document not found"
    error_instance = mock_document_error(DocumentNotFoundError(error_message))
    app.dependency_overrides[get_find_document_use_case] = lambda: error_instance
    response = client.get(f"/find/{checksum}")

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/problem+json"

    data = response.json()
    assert data["title"] == "Document Not Found"
    assert data["status"] == 404
    assert data["detail"] == error_message

    assert data["type"] == "/errors/not-found"
    assert data["instance"] == f"/find/{checksum}"