from fastapi.testclient import TestClient

from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.dependencies.dependencies import get_delete_document_use_case
from app.main import app

client = TestClient(app)

def test_delete_document_success():
    checksum = "DELETE-UNIQUE-CODE"
    expected_message = "Document with checksum DELETE-UNIQUE-CODE deleted successfully"

    class DeleteMock:
        def execute(self, unique_code):
            return {"message": expected_message}

    app.dependency_overrides[get_delete_document_use_case] = lambda: DeleteMock()

    response = client.delete(f"/delete/{checksum}")

    assert response.status_code == 200
    assert response.json()["message"] == expected_message


def test_delete_document_not_found(mock_document_error):
    checksum = "NON-EXISTENT-CODE"
    error_message = "The requested document does not exist."

    error_instance = mock_document_error(
        DocumentNotFoundError(error_message)
    )

    app.dependency_overrides[get_delete_document_use_case] = lambda: error_instance

    response = client.delete(f"/delete/{checksum}")

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/problem+json"

    data = response.json()

    assert data["status"] == 404
    assert data["title"] == "Document Not Found"
    assert data["detail"] == error_message
    assert data["type"] == "/errors/not-found"
    assert data["instance"] == f"/delete/{checksum}"
