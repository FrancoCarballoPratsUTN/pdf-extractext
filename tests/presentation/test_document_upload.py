import pytest
from fastapi.testclient import TestClient
from app.main import app 
from app.infrastructure.dependencies.dependencies import get_process_document_use_case 
from app.domain.exceptions.domain_exceptions import DocumentValidationError

client = TestClient(app)

def test_upload_pdf_structure(mock_document, mock_document_success, file_upload):
    app.dependency_overrides[get_process_document_use_case] = ( lambda: mock_document_success )
    response = client.post("/upload", files=file_upload)

    assert response.status_code == 201
    assert response.json()["file_name"] == mock_document.file_name


def test_upload_pdf_validation_error(mock_document_error, file_upload):
    error_msg = "Invalid PDF structure"
    error_instance = mock_document_error(DocumentValidationError(error_msg))
    app.dependency_overrides[get_process_document_use_case] = lambda: error_instance
    response = client.post("/upload", files=file_upload)

    assert response.status_code == 422
    assert response.headers["Content-Type"] == "application/problem+json"
    
    data = response.json()
    assert data["title"] == "Document Validation Error"
    assert data["detail"] == error_msg