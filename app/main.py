import uvicorn
from fastapi import FastAPI
from app.config.config_factory import settings
from app.logging.log_middleware import LogMiddleware
from app.logging.app_logger import log_queue_listener
from contextlib import asynccontextmanager
from app.events import (
    execute_backend_server_event_handler,
    terminate_backend_server_event_handler,
)
from app.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    ## Stop listening in queue
    log_queue_listener.stop()


def initialize_application() -> FastAPI:
    """
    This function initializes the FastAPI application. Therefore,
    configuration is set and db - connection will be established.
    """

    init = FastAPI(lifespan=lifespan,**settings.set_app_attributes) # type: ignore

    # add middleware
    init.add_middleware(LogMiddleware)

    # add router
    init.include_router(router=api_router)

    # add handlers
    init.add_event_handler("startup",execute_backend_server_event_handler())
    init.add_event_handler("shutdown",terminate_backend_server_event_handler())
    return init


app: FastAPI = initialize_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
    )
