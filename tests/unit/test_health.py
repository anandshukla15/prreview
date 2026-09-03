"""Unit tests for health and root endpoints."""

import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app
from app.config import Settings, get_settings


@pytest.mark.asyncio
async def test_health_check():
    """Verify GET /health returns 200 OK and expected structure."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "app" in data
    assert "version" in data
    assert "environment" in data
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_root_endpoint():
    """Verify GET / returns welcome payload and navigation links."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["docs_url"] == "/docs"
    assert data["health_url"] == "/health"


@pytest.mark.asyncio
async def test_health_check_custom_settings():
    """Verify health check respects dependency overrides."""
    custom_settings = Settings(
        APP_NAME="Custom Reviewer",
        APP_VERSION="9.9.9",
        APP_ENV="testing",
    )
    app.dependency_overrides[get_settings] = lambda: custom_settings

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["app"] == "Custom Reviewer"
        assert data["version"] == "9.9.9"
        assert data["environment"] == "testing"
    finally:
        app.dependency_overrides.clear()
