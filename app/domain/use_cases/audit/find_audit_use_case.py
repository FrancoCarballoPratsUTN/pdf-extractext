from app.domain.entities.audit_log import AuditLog
from app.domain.repositories.audit_log_repository import AuditLogRepository


class FindAuditLogsUseCase:
    """Use case for finding all audit logs with pagination."""

    def __init__(self, repo: AuditLogRepository):
        self._repo = repo

    def execute(self, skip: int, limit: int) -> list[AuditLog]:
        return self._repo.find_all(skip, limit)
