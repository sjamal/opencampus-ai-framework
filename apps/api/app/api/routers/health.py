from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session

from app.core.config import settings


router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health(
    session: AsyncSession = Depends(get_session),
):

    database_status = "unknown"

    try:
        await session.execute(text("SELECT 1"))
        database_status = "connected"

    except Exception:
        database_status = f"unavailable: {type(exc).__name__}"

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "database": database_status,
    }
