from fastapi.testclient import TestClient

from app.main import app

import pytest


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200

    body = response.json()

    assert body["application"] == "OpenCampus AI Framework"
