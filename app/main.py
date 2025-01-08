import uvicorn
from fastapi import FastAPI

from app.config.config_factory import settings
from app.events import (
    execute_backend_server_event_handler,
    terminate_backend_server_event_handler,
)
from app.router import api_router



def initialize_application() -> FastAPI:
    """
    This function initializes the FastAPI application. Therefore,
    configuration is set and db - connection will be established.
    """

    init = FastAPI(**settings.set_app_attributes)  # type: ignore
    init.include_router(router=api_router)

    init.add_event_handler(
        "startup",
        execute_backend_server_event_handler(),
    )

    init.add_event_handler(
        "shutdown",
        terminate_backend_server_event_handler(),
    )

    return init


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
