from pydantic import ConfigDict, Field
from datetime import datetime
from pydantic import BaseModel

class AuditLogSchema(BaseModel):
    """Response model for audit log entries."""
    action: str
    entity_type: str
    checksum: str
    details: dict | None = None
    performed_at: datetime
    id: str | None = Field(None, alias="_id", serialization_alias="_id")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
