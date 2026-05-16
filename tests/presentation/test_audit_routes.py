from fastapi.testclient import TestClient
from datetime import datetime
from app.main import app
from app.infrastructure.dependencies.dependencies import get_find_audit_use_case, get_find_audit_by_checksum
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.domain.entities.audit_log import Audit_Log

client = TestClient(app)


def test_get_audit_logs_success():
    class MockUseCase:
        """Mock use case to simulate the behavior of finding audit logs."""
        def execute(self, skip, limit):
            return [
                Audit_Log(
                    action="save", entity_type="Document", checksum="abc",
                    performed_at=datetime(2024, 1, 1, 12, 0, 0), id="id-1",
                ),
                Audit_Log(
                    action="delete", entity_type="Document", checksum="def",
                    details={"reason": "test"},
                    performed_at=datetime(2024, 6, 15, 10, 30, 0), id="id-2",
                ),
            ]

    app.dependency_overrides[get_find_audit_use_case] = lambda: MockUseCase()
    response = client.get("/audit/logs?skip=0&limit=10")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["action"] == "save"
    assert data[0]["checksum"] == "abc"
    assert data[1]["action"] == "delete"
    assert data[1]["checksum"] == "def"


def test_get_audit_logs_empty():
    class MockUseCase:
        """Mock use case to simulate the behavior of finding audit logs."""
        def execute(self, skip, limit):
            return []

    app.dependency_overrides[get_find_audit_use_case] = lambda: MockUseCase()
    response = client.get("/audit/logs")

    assert response.status_code == 200
    assert response.json() == []


def test_get_audit_logs_by_checksum_success():
    class MockUseCase:
        def execute(self, checksum):
            return [
                Audit_Log(
                    action="save", entity_type="Document", checksum=checksum,
                    performed_at=datetime(2024, 1, 1, 12, 0, 0), id="id-1",
                ),
            ]

    app.dependency_overrides[get_find_audit_by_checksum] = lambda: MockUseCase()
    response = client.get("/audit/logs/checksum/test-checksum")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["checksum"] == "test-checksum"


def test_get_audit_logs_by_checksum_not_found():
    class MockUseCase:
        def execute(self, checksum):
            raise DocumentNotFoundError("No audit logs found with checksum: nonexistent")

    app.dependency_overrides[get_find_audit_by_checksum] = lambda: MockUseCase()
    response = client.get("/audit/logs/checksum/nonexistent")

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/problem+json"

    data = response.json()
    assert data["title"] == "Document Not Found"
    assert data["status"] == 404
    assert "nonexistent" in data["detail"]


def test_get_audit_logs_by_checksum_multiple_results():
    class MockUseCase:
        def execute(self, checksum):
            return [
                Audit_Log(
                    action="save", entity_type="Document", checksum=checksum,
                    performed_at=datetime(2024, 1, 1, 12, 0, 0), id="id-1",
                ),
                Audit_Log(
                    action="update", entity_type="Document", checksum=checksum,
                    performed_at=datetime(2024, 1, 2, 12, 0, 0), id="id-2",
                ),
            ]

    app.dependency_overrides[get_find_audit_by_checksum] = lambda: MockUseCase()
    response = client.get("/audit/logs/checksum/multi")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == "id-1"
    assert data[1]["id"] == "id-2"
