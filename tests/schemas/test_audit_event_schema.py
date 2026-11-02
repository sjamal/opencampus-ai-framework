from datetime import datetime

import pytest

from pydantic import ValidationError

from app.models.audit_event import AuditEvent
from app.schemas.audit_event import AuditEventCreate, AuditEventResponse


def test_create_schema_accepts_valid_payload():
    payload = AuditEventCreate(event_type="SCHEMA_TEST", description="Valid")

    assert payload.event_type == "SCHEMA_TEST"
    assert payload.description == "Valid"


def test_create_schema_description_is_optional():
    assert AuditEventCreate(event_type="SCHEMA_TEST").description is None


def test_create_schema_requires_event_type():
    with pytest.raises(ValidationError):
        AuditEventCreate(description="Missing type")


def test_create_schema_limits_event_type_length():
    # Matches the String(100) column on the AuditEvent model.
    AuditEventCreate(event_type="X" * 100)

    with pytest.raises(ValidationError):
        AuditEventCreate(event_type="X" * 101)


def test_response_schema_reads_from_model():
    event = AuditEvent(
        id=1,
        event_type="SCHEMA_TEST",
        description=None,
        created_at=datetime(2026, 1, 1),
    )

    response = AuditEventResponse.model_validate(event)

    assert response.id == 1
    assert response.event_type == "SCHEMA_TEST"
    assert response.description is None
    assert response.created_at == datetime(2026, 1, 1)
