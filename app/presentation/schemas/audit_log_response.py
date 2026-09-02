from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AuditLogSchema(BaseModel):
    """Response model for audit log entries."""

    action: str
    entity_type: str
    checksum: str
    details: str | None = None
    performed_at: datetime
    id: str | None = Field(None, alias="_id", serialization_alias="_id")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
