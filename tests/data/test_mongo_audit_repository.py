import pytest
import mongomock
from datetime import datetime
from app.domain.entities.audit_log import Audit_Log
from app.domain.exceptions.domain_exceptions import DocumentNotFoundError
from app.infrastructure.persistence.repositories.mongo_audit_repository import MongoAuditLogRepository


@pytest.fixture
def audit_repo():
    """
    Instancia el repositorio inyectando un cliente sincrónico de mongomock.
    Cumple con Inyección de Dependencias (SOLID) y mantiene el setup simple (KISS).
    """
    client = mongomock.MongoClient()
    db = client["test_db"]
    collection = db["audit_logs"]
    repo = MongoAuditLogRepository(db)
    repo._collection = collection
    return repo



def test_save_audit_log(audit_repo):
    log = Audit_Log(
        action="save",
        entity_type="Document",
        checksum="abc123",
        details={"file": "test.pdf"},
        performed_at=datetime(2024, 1, 1, 12, 0, 0),
    )

    saved = audit_repo.save(log)

    assert saved.id is not None
    assert saved.action == "save"
    assert saved.checksum == "abc123"


def test_find_all_returns_all_logs(audit_repo):
    logs = [
        Audit_Log(action="save", entity_type="Document", checksum="cs1"),
        Audit_Log(action="delete", entity_type="Document", checksum="cs2"),
        Audit_Log(action="update", entity_type="Document", checksum="cs3"),
    ]
    for log in logs:
        audit_repo.save(log)

    result = audit_repo.find_all(skip=0, limit=10)

    assert len(result) == 3
    assert result[0].checksum == "cs1"
    assert result[1].checksum == "cs2"
    assert result[2].checksum == "cs3"


def test_find_all_with_pagination(audit_repo):
    for i in range(10):
        audit_repo.save(
            Audit_Log(action="save", entity_type="Document", checksum=f"cs{i}")
        )

    result = audit_repo.find_all(skip=3, limit=4)

    assert len(result) == 4
    assert result[0].checksum == "cs3"
    assert result[3].checksum == "cs6"


def test_find_by_checksum_returns_matching_logs(audit_repo):
    audit_repo.save(Audit_Log(action="save", entity_type="Document", checksum="target"))
    audit_repo.save(Audit_Log(action="delete", entity_type="Document", checksum="other"))
    audit_repo.save(Audit_Log(action="update", entity_type="Document", checksum="target"))

    result = audit_repo.find_by_checksum("target")

    assert len(result) == 2
    assert all(log.checksum == "target" for log in result)


def test_find_by_checksum_raises_error_when_not_found(audit_repo):
    with pytest.raises(DocumentNotFoundError) as exc_info:
        audit_repo.find_by_checksum("nonexistent")

    assert "No audit logs found" in str(exc_info.value.detail)


def test_save_assigns_unique_ids(audit_repo):
    log1 = Audit_Log(action="save", entity_type="Document", checksum="cs1")
    log2 = Audit_Log(action="save", entity_type="Document", checksum="cs2")

    saved1 = audit_repo.save(log1)
    saved2 = audit_repo.save(log2)

    assert saved1.id is not None
    assert saved2.id is not None
    assert saved1.id != saved2.id