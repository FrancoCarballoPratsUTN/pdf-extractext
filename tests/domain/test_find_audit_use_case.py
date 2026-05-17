from app.domain.entities.audit_log import AuditLog
from app.domain.use_cases.audit.find_audit_use_case import FindAuditLogsUseCase


class MockAuditRepository:
    """
    A mock implementation of the Audit_LogRepository for testing purposes.
    It allows us to simulate the behavior of the repository without needing a real database.
     - data_pool: A list of AuditLog objects to return when find_all is called.
     - captured_skip: Captures the 'skip' parameter passed to find_all for verification.
     - captured_limit: Captures the 'limit' parameter passed to find_all for verification.
    """
    def __init__(self, data_pool=None):
        self.data_pool = data_pool if data_pool is not None else []
        self.captured_skip = None
        self.captured_limit = None

    def find_all(self, skip: int, limit: int):
        self.captured_skip = skip
        self.captured_limit = limit
        
        if len(self.data_pool) <= limit and skip == 0:
            return self.data_pool
        return self.data_pool[skip : skip + limit]

def test_find_audit_logs_execute_returns_list():
    expected_logs = [
        AuditLog(action="save", entity_type="Document", checksum="abc"),
        AuditLog(action="delete", entity_type="Document", checksum="def"),
    ]
    repo = MockAuditRepository(data_pool=expected_logs)
    use_case = FindAuditLogsUseCase(repo)

    result = use_case.execute(skip=0, limit=10)

    assert result == expected_logs
    assert len(result) == 2


def test_find_audit_logs_with_pagination():
    all_logs = [
        AuditLog(action="save", entity_type="Document", checksum=f"checksum{i}")
        for i in range(20)
    ]
    repo = MockAuditRepository(data_pool=all_logs)
    use_case = FindAuditLogsUseCase(repo)

    result = use_case.execute(skip=5, limit=5)

    assert len(result) == 5
    assert result[0].checksum == "checksum5"
    assert result[4].checksum == "checksum9"

def test_find_audit_logs_empty_result():
    repo = MockAuditRepository(data_pool=[])
    use_case = FindAuditLogsUseCase(repo)

    result = use_case.execute(skip=0, limit=10)

    assert result == []