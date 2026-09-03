"""Application Configuration Module using Pydantic Settings."""

from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration for the Autonomous Code Reviewer."""

    # Application settings
    APP_NAME: str = "Autonomous Code Reviewer"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/prreview"
    DATABASE_SYNC_URL: Optional[str] = "postgresql+psycopg2://postgres:postgres@localhost:5432/prreview"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # GitHub Integration
    GITHUB_TOKEN: Optional[str] = None
    GITHUB_WEBHOOK_SECRET: Optional[str] = None

    # LLM Settings
    GEMINI_API_KEY: Optional[str] = None
    LLM_PROVIDER: str = "gemini"
    LLM_MODEL: str = "gemini-2.5-flash"

    # HITL & Risk Policies
    HITL_ENABLED: bool = True
    AUTO_PUBLISH_SEVERITY_THRESHOLD: str = "LOW"
    HIGH_RISK_CONFIDENCE_THRESHOLD: float = 0.90
    MIN_CONFIDENCE_THRESHOLD: float = 0.70

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )


@lru_cache()
def get_settings() -> Settings:
    """Provide cached settings instance."""
    return Settings()
