from app.domain.entities.audit_log import Audit_Log
from app.domain.repositories.audit_log_repository import Audit_LogRepository

class FindAuditLogsByChecksumUseCase:
    """Use case for finding audit logs by document checksum."""
    def __init__(self, repo: Audit_LogRepository):
        self._repo = repo
    def execute(self, checksum: str) -> list[Audit_Log]:
        return self._repo.find_by_checksum(checksum)