"""Structured logging configuration for the application."""

import logging
import sys
from app.config import get_settings


def setup_logging() -> logging.Logger:
    """Configure structured console logging based on environment settings."""
    settings = get_settings()
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
    )

    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )

    logger = logging.getLogger("autonomous_reviewer")
    logger.setLevel(log_level)
    return logger


logger = setup_logging()
