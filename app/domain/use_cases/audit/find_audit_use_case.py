from app.domain.entities.audit_log import Audit_Log
from app.domain.repositories.audit_log_repository import Audit_LogRepository

class FindAuditLogsUseCase:
    """Use case for finding all audit logs with pagination."""
    def __init__(self, repo: Audit_LogRepository): 
        self._repo = repo
    def execute(self, skip: int, limit: int) -> list[Audit_Log]:
        return  self._repo.find_all(skip, limit)