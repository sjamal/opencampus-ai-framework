"""
Service tests use a fake repository, so they run without a database.

This is the payoff of the repository/service split (ADR-0013): business
logic can be tested in isolation from persistence.
"""

from datetime import datetime

import pytest

from app.models.audit_event import AuditEvent
from app.services.audit_event_service import AuditEventService


pytestmark = pytest.mark.asyncio

SESSION = object()


class FakeAuditEventRepository:
    """In-memory stand-in for AuditEventRepository that records calls."""

    def __init__(self):
        self.events: list[AuditEvent] = []
        self.calls: list[tuple] = []

    async def create(self, session, *, event_type, description=None):
        self.calls.append(("create", session, event_type, description))

        event = AuditEvent(
            id=len(self.events) + 1,
            event_type=event_type,
            description=description,
            created_at=datetime(2026, 1, 1),
        )
        self.events.append(event)

        return event

    async def get(self, session, event_id):
        self.calls.append(("get", session, event_id))

        return next((e for e in self.events if e.id == event_id), None)

    async def list(self, session):
        self.calls.append(("list", session))

        return list(reversed(self.events))


async def test_record_event_creates_through_repository():
    repository = FakeAuditEventRepository()
    service = AuditEventService(repository)

    event = await service.record_event(
        SESSION,
        event_type="SERVICE_TEST",
        description="Recorded",
    )

    assert event.event_type == "SERVICE_TEST"
    assert event.description == "Recorded"
    assert repository.calls == [("create", SESSION, "SERVICE_TEST", "Recorded")]


async def test_get_event_returns_existing_event():
    repository = FakeAuditEventRepository()
    service = AuditEventService(repository)

    created = await service.record_event(SESSION, event_type="SERVICE_TEST")

    assert await service.get_event(SESSION, created.id) is created


async def test_get_event_returns_none_when_missing():
    service = AuditEventService(FakeAuditEventRepository())

    assert await service.get_event(SESSION, 999) is None


async def test_list_events_returns_repository_results():
    repository = FakeAuditEventRepository()
    service = AuditEventService(repository)

    first = await service.record_event(SESSION, event_type="SERVICE_TEST")
    second = await service.record_event(SESSION, event_type="SERVICE_TEST")

    assert await service.list_events(SESSION) == [second, first]
