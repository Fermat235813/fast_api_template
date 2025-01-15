"""router

Here every router from application packages ist added to basic model

In this file the basic models of database schema is defined.

Classification: Unclassified
Autor: Lothar Janssen
"""
from fastapi import APIRouter
from app.config.router import config_router
from app.logging.router import log_router
from app.auth.router import auth_router

api_router = APIRouter()

api_router.include_router(config_router, tags=["settings"])
api_router.include_router(log_router, tags=["logging"])
api_router.include_router(auth_router, tags=["auth"])