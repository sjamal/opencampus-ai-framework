from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers.health import router as health_router
from app.core.config import settings
from app.core.logging import logger, setup_logging

from app.api.routers import audit

@asynccontextmanager
async def lifespan(app: FastAPI):

    setup_logging()

    logger.info(
        "Starting %s version %s",
        settings.app_name,
        settings.app_version,
    )

    yield

    logger.info(
        "Stopping %s",
        settings.app_name,
    )


app = FastAPI(
    title="OpenCampus AI Framework API",
    description="Enterprise AI Workflow Framework",
    version=settings.app_version,
    lifespan=lifespan,
)


app.include_router(health_router)

app.include_router(
    audit.router
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "application": "OpenCampus AI Framework",
        "status": "running",
        "version": "0.1.0",
    }
