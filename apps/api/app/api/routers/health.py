from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session

from app.core.config import settings
from app.core.logging import logger


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
        logger.exception("Database health check failed")
        database_status = "unavailable"

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
        "database": database_status,
    }
