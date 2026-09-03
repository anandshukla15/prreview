"""Health check endpoint."""

from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.dependencies import get_app_settings
from app.config import Settings

router = APIRouter(tags=["Health"])


class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
    environment: str
    timestamp: str


@router.get("/health", response_model=HealthResponse)
async def health_check(settings: Settings = Depends(get_app_settings)) -> HealthResponse:
    """Return application operational status and environment metadata."""
    return HealthResponse(
        status="ok",
        app=settings.APP_NAME,
        version=settings.APP_VERSION,
        environment=settings.APP_ENV,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
