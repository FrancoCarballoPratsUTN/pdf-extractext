from app.domain.entities.audit_log import Audit_Log
from app.domain.use_cases.audit.find_audit_by_checksum_use_case import FindAuditLogsByChecksumUseCase


class MockAuditRepository:
    """
    A mock implementation of the Audit_LogRepository for testing purposes.
    It allows us to simulate the behavior of the repository without needing a real database.
        - return_value: A list of Audit_Log objects to return when find_by_checksum is called.
        - captured_checksum: Captures the 'checksum' parameter passed to find_by_checksum for verification.
    """
    def __init__(self, return_value=None):
        self.return_value = return_value if return_value is not None else []
        self.captured_checksum = None

    def find_by_checksum(self, checksum: str):
        self.captured_checksum = checksum
        return self.return_value

def test_find_by_checksum_returns_matching_logs():
    expected = [
        Audit_Log(action="save", entity_type="Document", checksum="abc123"),
        Audit_Log(action="update", entity_type="Document", checksum="abc123"),
    ]
    
    repo = MockAuditRepository(return_value=expected)
    use_case = FindAuditLogsByChecksumUseCase(repo)
    
    result = use_case.execute("abc123")

    assert result == expected
    assert len(result) == 2


def test_find_by_checksum_returns_empty_list():
    repo = MockAuditRepository(return_value=[])
    use_case = FindAuditLogsByChecksumUseCase(repo)
    
    result = use_case.execute("nonexistent")

    assert result == []


def test_find_by_checksum_passes_correct_checksum():
    repo = MockAuditRepository()
    use_case = FindAuditLogsByChecksumUseCase(repo)
    
    use_case.execute("specific-checksum")

    assert repo.captured_checksum == "specific-checksum"