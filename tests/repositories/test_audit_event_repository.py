import pytest

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_event import AuditEvent
from app.repositories.audit_event_repository import AuditEventRepository


@pytest.mark.asyncio
async def test_create_audit_event(db_session: AsyncSession):
    # Clean the table to keep the test deterministic.
    await db_session.execute(delete(AuditEvent))
    await db_session.commit()

    repository = AuditEventRepository()

    event = await repository.create(
        db_session,
        event_type="UNIT_TEST",
        description="Repository test",
    )

    assert event.id is not None
    assert event.event_type == "UNIT_TEST"
    assert event.description == "Repository test"
    assert event.created_at is not None
