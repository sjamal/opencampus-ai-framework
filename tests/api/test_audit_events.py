import pytest

from httpx import AsyncClient


pytestmark = pytest.mark.asyncio

# Largest PostgreSQL integer; never reached by test data.
MISSING_EVENT_ID = 2_147_483_647


async def create_event(client: AsyncClient, **payload) -> dict:
    response = await client.post("/audit-events", json=payload)
    assert response.status_code == 200
    return response.json()


async def test_create_audit_event(client: AsyncClient):
    response = await client.post(
        "/audit-events",
        json={"event_type": "API_TEST", "description": "Created via API"},
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body["id"], int)
    assert body["event_type"] == "API_TEST"
    assert body["description"] == "Created via API"
    assert body["created_at"]


async def test_create_audit_event_without_description(client: AsyncClient):
    body = await create_event(client, event_type="API_TEST")

    assert body["description"] is None


async def test_create_audit_event_requires_event_type(client: AsyncClient):
    response = await client.post("/audit-events", json={"description": "No type"})

    assert response.status_code == 422


async def test_create_audit_event_rejects_long_event_type(client: AsyncClient):
    response = await client.post("/audit-events", json={"event_type": "X" * 101})

    assert response.status_code == 422


async def test_get_audit_event(client: AsyncClient):
    created = await create_event(client, event_type="API_TEST", description="Fetch me")

    response = await client.get(f"/audit-events/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


async def test_get_missing_audit_event_returns_404(client: AsyncClient):
    response = await client.get(f"/audit-events/{MISSING_EVENT_ID}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Audit event not found"}


async def test_get_audit_event_rejects_non_integer_id(client: AsyncClient):
    response = await client.get("/audit-events/not-a-number")

    assert response.status_code == 422


async def test_list_audit_events(client: AsyncClient):
    first = await create_event(client, event_type="API_TEST", description="First")
    second = await create_event(client, event_type="API_TEST", description="Second")

    response = await client.get("/audit-events")

    assert response.status_code == 200

    body = response.json()
    ids = [item["id"] for item in body["items"]]

    assert body["total"] == len(body["items"])
    # Newest events are listed first.
    assert ids.index(second["id"]) < ids.index(first["id"])
