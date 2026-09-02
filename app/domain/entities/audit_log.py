from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class AuditLog:
    action: str
    entity_type: str
    checksum: str
    details: str | None = None
    performed_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    _id: str | None = None
