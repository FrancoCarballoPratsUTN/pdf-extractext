import logging
from datetime import UTC, datetime

from app.domain.entities.audit_log import AuditLog
from app.domain.repositories.audit_log_repository import AuditLogRepository

logger = logging.getLogger(__name__)


class AuditDecorator:
    """
    Decorator for use cases to log actions in the audit log.
    """

    def __init__(
        self,
        use_case,
        audit_repo: AuditLogRepository,
        action: str,
        entity_type: str,
        checksum_extractor,
    ):
        self._use_case = use_case
        self._audit_repo = audit_repo
        self._action = action
        self._entity_type = entity_type
        self._checksum_extractor = checksum_extractor

    def execute(self, *args, **kwargs):
        """Executes the use case and logs the action in the audit log.
        Args:
            *args: Positional arguments for the use case.
            **kwargs: Keyword arguments for the use case.
        Returns:
                The result of the use case execution."""
        try:
            result = self._use_case.execute(*args, **kwargs)

            checksum = self._checksum_extractor(result, *args, **kwargs)
            log = AuditLog(
                action=self._action,
                entity_type=self._entity_type,
                checksum=checksum,
                details=(
                    f"Action {self._action} performed on {self._entity_type} "
                    f"with checksum {checksum}"
                ),
                performed_at=datetime.now(UTC),
            )

            self._audit_repo.save(log)
            logger.info(
                "Audit log created",
                extra={
                    "action": self._action,
                    "entity_type": self._entity_type,
                    "checksum": checksum,
                },
            )
            return result
        except Exception as audit_error:
            logger.critical(f"Error executing use case: {audit_error}", exc_info=True)
            raise
