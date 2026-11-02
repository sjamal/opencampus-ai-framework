from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_event import AuditEvent

from sqlalchemy import select

class AuditEventRepository:
    """
    Database operations for audit events.
    """

    async def create(
        self,
        session: AsyncSession,
        *,
        event_type: str,
        description: str | None = None,
        ) -> AuditEvent:

        event = AuditEvent(
            event_type=event_type,
            description=description,
        )

        session.add(event)

        await session.commit()
        await session.refresh(event)

        return event

    async def get(
        self,
        session: AsyncSession,
        event_id: int,
        ) -> AuditEvent | None:

        return await session.get(AuditEvent, event_id)


    async def list(
        self,
        session: AsyncSession,
        ) -> list[AuditEvent]:

        result = await session.execute(
            select(AuditEvent).order_by(AuditEvent.created_at.desc())
        )

        return list(result.scalars())
