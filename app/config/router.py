from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from app.config.config_factory import settings

config_router = APIRouter()


@config_router.get("/settings")
async def get_current_config() -> Mapping[str, Any]:
    """
    Return all current values based on .env file.
    """
    return vars(settings)
