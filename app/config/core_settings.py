import logging

import decouple
from pydantic_settings import BaseSettings

from app.config.constants import PROJECT_DESCRIPTION, TAGS_METADATA


class CoreSettings(BaseSettings):
    TITLE: str = "TEMPLATE"
    VERSION: str = "0.1.0"
    DESCRIPTION: str | None = PROJECT_DESCRIPTION
    SUMMARY: str | None = None
    DEBUG: bool = False
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""
    OPENAPI_TAGS: list[dict[str, str]] | None = TAGS_METADATA

    SERVER_HOST: str = decouple.config("SERVER_HOST", cast=str)
    SERVER_PORT: int = decouple.config("SERVER_PORT", cast=int)
    SERVER_WORKERS: int = decouple.config("SERVER_WORKERS", cast=int)

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    @property
    def set_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom
        values defined in `CoreSettings`.
        """
        return {
            "openapi_tags": self.OPENAPI_TAGS,  # type: ignore
            "title": self.TITLE,
            "version": self.VERSION,
            "summary": self.SUMMARY,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
