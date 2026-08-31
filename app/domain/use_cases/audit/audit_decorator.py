import logging
from datetime import UTC, datetime

from app.domain.entities.audit_log import AuditLog
from app.domain.repositories.audit_log_repository import Audit_LogRepository

logger = logging.getLogger(__name__)


class AuditDecorator:
    """
    Decorator for use cases to log actions in the audit log.
    """

    def __init__(
        self, use_case, audit_repo: Audit_LogRepository, action: str, entity_type: str
    ):
        self._use_case = use_case
        self._audit_repo = audit_repo
        self._action = action
        self._entity_type = entity_type
        self._checksum = None

    def execute(self, *args, **kwargs):
        """Executes the use case and logs the action in the audit log.
        Args:
            *args: Positional arguments for the use case.
            **kwargs: Keyword arguments for the use case.
        Returns:
                The result of the use case execution."""
        try:
            result = self._use_case.execute(*args, **kwargs)

            checksum = (
                result.checksum
                if hasattr(result, "checksum")
                else kwargs.get("checksum", "")
            )
            self._checksum = checksum
            log = AuditLog(
                action=self._action,
                entity_type=self._entity_type,
                checksum=self._checksum,
                details=f"Action {self._action} performed on {self._entity_type} with checksum {self._checksum}",
                performed_at=datetime.now(UTC),
            )

            self._audit_repo.save(log)
            logger.info(
                "Audit log created",
                extra={
                    "action": self._action,
                    "entity_type": self._entity_type,
                    "checksum": self._checksum,
                },
            )
            return result
        except Exception as audit_error:
            logger.critical(f"Error executing use case: {audit_error}", exc_info=True)
            raise
