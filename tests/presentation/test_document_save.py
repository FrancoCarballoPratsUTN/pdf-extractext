from fastapi.testclient import TestClient
from dataclasses import asdict
from app.main import app
from app.infrastructure.dependencies.dependencies import get_save_document_use_case
from app.domain.exceptions.domain_exceptions import DocumentAlreadyExistsError

client = TestClient(app)

def test_save_document_success(mock_document_success, mock_document):

    app.dependency_overrides[get_save_document_use_case] = lambda: mock_document_success

    document_data = asdict(mock_document)
    document_data["date"] = str(document_data["date"])
    
    response = client.post("/save", json=document_data)
    
    assert response.status_code == 200
    assert response.json()["checksum"] == mock_document.checksum


def test_save_document_already_exists(mock_document_error, mock_document):

    error_instance = mock_document_error(DocumentAlreadyExistsError("Document already exists"))

    app.dependency_overrides[get_save_document_use_case] = lambda: error_instance

    document_data = asdict(mock_document)
    document_data["date"] = str(document_data["date"])
    
    response = client.post("/save", json=document_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Document already exists"