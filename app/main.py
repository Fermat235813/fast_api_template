import uvicorn
from fastapi import FastAPI

from app.config.config_factory import settings
from app.router import api_router


def initialize_application() -> FastAPI:
    init = FastAPI(**settings.set_app_attributes)  # type: ignore
    init.include_router(router=api_router)
    return init


app: FastAPI = initialize_application()


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
