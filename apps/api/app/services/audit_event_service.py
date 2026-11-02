from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_event import AuditEvent
from app.repositories.audit_event_repository import AuditEventRepository


class AuditEventService:
    """Business logic for audit events."""

    def __init__(
        self,
        repository: AuditEventRepository,
    ):
        self.repository = repository

    async def record_event(
        self,
        session: AsyncSession,
        *,
        event_type: str,
        description: str | None = None,
    ) -> AuditEvent:

        return await self.repository.create(
            session,
            event_type=event_type,
            description=description,
        )

    async def get_event(
        self,
        session: AsyncSession,
        event_id: int,
    ) -> AuditEvent | None:

        return await self.repository.get(
            session,
            event_id,
        )

    async def list_events(
        self,
        session: AsyncSession,
    ) -> list[AuditEvent]:

        return await self.repository.list(session)
