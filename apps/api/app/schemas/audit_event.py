from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AuditEventCreate(BaseModel):
    event_type: str = Field(..., max_length=100)
    description: str | None = None


class AuditEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    event_type: str
    description: str | None
    created_at: datetime


class AuditEventList(BaseModel):
    items: list[AuditEventResponse]
    total: int
