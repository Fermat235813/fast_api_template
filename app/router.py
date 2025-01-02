from fastapi import APIRouter

from app.generic.router import generic_router

api_router = APIRouter()

api_router.include_router(generic_router, tags=["generic"])
