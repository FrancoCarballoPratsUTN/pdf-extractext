import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.dependencies.dependencies import get_delete_document_use_case
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError

client = TestClient(app)

def test_delete_document_success():

    checksum = "DELETE-UNIQUE-CODE"

    class DeleteMock:
        def execute(self, unique_code):
            return {"message": f"Document with checksum {unique_code} deleted successfully"}
            
    app.dependency_overrides[get_delete_document_use_case] = lambda: DeleteMock()

    response = client.delete(f"/delete/{checksum}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Document with checksum {checksum} deleted successfully"


def test_delete_document_not_found(mock_document_error):

    checksum = "UNIQUE-CODE"

    error_instance = mock_document_error(DocumentNotFoundError("Document not found"))
    
    app.dependency_overrides[get_delete_document_use_case] = lambda: error_instance

    response = client.delete(f"/delete/{checksum}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Document not found"