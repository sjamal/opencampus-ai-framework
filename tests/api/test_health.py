import pytest

from httpx import AsyncClient


pytestmark = pytest.mark.asyncio


async def test_health_endpoint(client: AsyncClient):
    response = await client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["database"] == "connected"


async def test_root_endpoint(client: AsyncClient):
    response = await client.get("/")

    assert response.status_code == 200

    body = response.json()

    assert body["application"] == "OpenCampus AI Framework"
