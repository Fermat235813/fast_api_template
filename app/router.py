from fastapi import APIRouter

from app.config.router import config_router
from app.logging.router import log_router

api_router = APIRouter()

api_router.include_router(config_router, tags=["settings"])
api_router.include_router(log_router)