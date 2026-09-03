"""Main FastAPI application entrypoint."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.health import router as health_router
from app.config import get_settings
from app.observability.logging import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application startup and shutdown lifespan context."""
    settings = get_settings()
    logger.info("Starting up %s (v%s) in [%s] mode...", settings.APP_NAME, settings.APP_VERSION, settings.APP_ENV)
    yield
    logger.info("Shutting down %s...", settings.APP_NAME)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Autonomous Multi-Agent Code Review & Security Auditor API",
        lifespan=lifespan,
    )

    # Cross-Origin Resource Sharing
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register Routers
    app.include_router(health_router)

    @app.get("/", tags=["Root"])
    async def root():
        return {
            "message": f"Welcome to {settings.APP_NAME}",
            "version": settings.APP_VERSION,
            "docs_url": "/docs",
            "health_url": "/health",
        }

    return app


app = create_app()
