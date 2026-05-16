from pydantic import ConfigDict
from datetime import datetime
from pydantic import BaseModel

class AuditLogSchema(BaseModel):
    """Response model for audit log entries."""
    action: str
    entity_type: str
    checksum: str
    details: dict | None = None
    performed_at: datetime
    id: str | None = None 
    model_config = ConfigDict(from_attributes=True)
