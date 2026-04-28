import pytest
from fastapi.testclient import TestClient
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.main import app
from app.infrastructure.dependencies.dependencies import get_update_document_use_case

client = TestClient(app)

def test_update_document_success(mock_document_success):

    checksum = "UPDATE-CODE"
    new_data = {"text": "Updated content"}
    app.dependency_overrides[get_update_document_use_case] = lambda: mock_document_success
    
    response = client.put(f"/update/{checksum}", json=new_data)
    
    assert response.status_code == 200
    assert response.json()["text"] == new_data["text"]
    assert response.json()["checksum"] == checksum


def test_update_document_not_found(mock_document_error):

    error_instance = mock_document_error(DocumentNotFoundError("Document not found"))
    app.dependency_overrides[get_update_document_use_case] = lambda: error_instance
    response = client.put("/update/not-exist", json={"text": "nothing"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Document not found"