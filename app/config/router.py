"""Logging router
Here the main entry points of logging are added.

This file contains the following
functions:

    * get_current_config - return the current configuration

Classification: Unclassified
Autor: Lothar Janssen
"""
from collections.abc import Mapping
from typing import Any
from fastapi import APIRouter
from app.config.service import settings

config_router = APIRouter()


@config_router.get("/settings")
async def get_current_config() -> Mapping[str, Any]:
    """
    Return the current configuration
    :return: Return all current values based on .env file.
    """
    return vars(settings)
