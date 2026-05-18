from datetime import datetime, timezone
from app.domain.mappers.to_dto import to_audit_log_dto
from app.domain.repositories.audit_log_repository import Audit_LogRepository

class AuditDecorator:
    """
    Decorator for use cases to log actions in the audit log.
    """
    def __init__(self, use_case, audit_repo: Audit_LogRepository, action: str, entity_type: str):
        self._use_case = use_case
        self._audit_repo = audit_repo
        self._action = action
        self._entity_type = entity_type
        self._checksum = None

    def execute(self, *args, **kwargs):
        """ Executes the use case and logs the action in the audit log.
            Args:
                *args: Positional arguments for the use case.
                **kwargs: Keyword arguments for the use case.
            Returns:
                    The result of the use case execution."""

        result = self._use_case.execute(*args, **kwargs)

        checksum = result.checksum if hasattr(result, 'checksum') else kwargs.get('checksum', '')
        self._checksum = checksum
        log = to_audit_log_dto({
            "action": self._action,
            "entity_type": self._entity_type,
            "checksum": self._checksum,
            "details": None,
            "performed_at": datetime.now(timezone.utc),
            "_id": None
        })

        self._audit_repo.save(log)
        return result