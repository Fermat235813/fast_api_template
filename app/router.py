from fastapi import APIRouter

from app.config.router import config_router

api_router = APIRouter()

api_router.include_router(config_router, tags=["settings"])
