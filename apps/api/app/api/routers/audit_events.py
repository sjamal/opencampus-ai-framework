from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.repositories.audit_event_repository import AuditEventRepository
from app.schemas.audit_event import (
    AuditEventCreate,
    AuditEventList,
    AuditEventResponse,
)
from app.services.audit_event_service import AuditEventService

router = APIRouter(
    prefix="/audit-events",
    tags=["Audit Events"],
)


def get_audit_service() -> AuditEventService:
    return AuditEventService(AuditEventRepository())


@router.post("", response_model=AuditEventResponse)
async def create_audit_event(
    payload: AuditEventCreate,
    session: AsyncSession = Depends(get_session),
    service: AuditEventService = Depends(get_audit_service),
):

    return await service.record_event(
        session,
        event_type=payload.event_type,
        description=payload.description,
    )


@router.get("", response_model=AuditEventList)
async def list_audit_events(
    session: AsyncSession = Depends(get_session),
    service: AuditEventService = Depends(get_audit_service),
):

    events = await service.list_events(session)

    return AuditEventList(
        items=events,
        total=len(events),
    )


@router.get("/{event_id}", response_model=AuditEventResponse)
async def get_audit_event(
    event_id: int,
    session: AsyncSession = Depends(get_session),
    service: AuditEventService = Depends(get_audit_service),
):

    event = await service.get_event(session, event_id)

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Audit event not found",
        )

    return event
