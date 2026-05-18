from dataclasses import field
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class AuditLog:
    action: str
    entity_type: str
    checksum: str
    details: dict | None = None
    performed_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    _id: str | None = None 
