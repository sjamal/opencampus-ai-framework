import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.audit_event_repository import AuditEventRepository


pytestmark = pytest.mark.asyncio

# Largest PostgreSQL integer; never reached by test data.
MISSING_EVENT_ID = 2_147_483_647


async def test_create_audit_event(db_session: AsyncSession):
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


async def test_create_audit_event_without_description(db_session: AsyncSession):
    repository = AuditEventRepository()

    event = await repository.create(db_session, event_type="UNIT_TEST")

    assert event.description is None


async def test_get_audit_event(db_session: AsyncSession):
    repository = AuditEventRepository()

    created = await repository.create(db_session, event_type="UNIT_TEST")
    fetched = await repository.get(db_session, created.id)

    assert fetched is not None
    assert fetched.id == created.id
    assert fetched.event_type == "UNIT_TEST"


async def test_get_missing_audit_event_returns_none(db_session: AsyncSession):
    repository = AuditEventRepository()

    assert await repository.get(db_session, MISSING_EVENT_ID) is None


async def test_list_audit_events_newest_first(db_session: AsyncSession):
    repository = AuditEventRepository()

    first = await repository.create(db_session, event_type="UNIT_TEST")
    second = await repository.create(db_session, event_type="UNIT_TEST")

    ids = [event.id for event in await repository.list(db_session)]

    assert first.id in ids
    assert ids.index(second.id) < ids.index(first.id)
