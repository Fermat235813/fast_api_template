import decouple

from pydantic_settings import BaseSettings
from app.config.constants import PROJECT_DESCRIPTION, TAGS_METADATA


class AbstractSettings(BaseSettings):
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
    ENVIRONMENT: str | None = None
    OPENAPI_TAGS: list[dict[str, str]] | None = TAGS_METADATA

    DB_POSTGRES_HOST: str = decouple.config("POSTGRES_HOST", cast=str)
    DB_POSTGRES_NAME: str = decouple.config("POSTGRES_DB", cast=str)
    DB_POSTGRES_PASSWORD: str = decouple.config("POSTGRES_PASSWORD", cast=str)
    DB_POSTGRES_PORT: int = decouple.config("POSTGRES_PORT", cast=int)
    DB_POSTGRES_SCHEMA: str = decouple.config("POSTGRES_SCHEMA", cast=str)
    DB_POSTGRES_ASYNC_SCHEMA: str = decouple.config("POSTGRES_ASYNC_SCHEMA", cast=str)
    DB_POSTGRES_USERNAME: str = decouple.config("POSTGRES_USERNAME", cast=str)

    DB_MAX_POOL_CON: int = decouple.config("DB_MAX_POOL_CON", cast=int)
    DB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int)
    DB_POOL_OVERFLOW: int = decouple.config("DB_POOL_OVERFLOW", cast=int)
    DB_TIMEOUT: int = decouple.config("DB_TIMEOUT", cast=int)
    IS_DB_ECHO_LOG: bool = decouple.config("IS_DB_ECHO_LOG", cast=bool)
    IS_DB_FORCE_ROLLBACK: bool = decouple.config("IS_DB_FORCE_ROLLBACK", cast=bool)
    IS_DB_EXPIRE_ON_COMMIT: bool = decouple.config("IS_DB_EXPIRE_ON_COMMIT", cast=bool)

    SERVER_HOST: str = decouple.config("SERVER_HOST", cast=str)
    SERVER_PORT: int = decouple.config("SERVER_PORT", cast=int)
    SERVER_WORKERS: int = decouple.config("SERVER_WORKERS", cast=int)

    LOG_LEVEL: str = decouple.config("LOG_LEVEL", cast=str)
    LOG_FILE_PATH: str = decouple.config("LOG_FILE_PATH", cast=str)
    LOG_FORMAT_PATTERN: str = decouple.config("LOG_FORMAT_PATTERN", cast=str)
    LOG_FILE: bool = decouple.config("LOG_FILE", cast=bool)
    LOG_CONSOLE: bool = decouple.config("LOG_CONSOLE", cast=bool)
    LOG_QUEUE: bool = decouple.config("LOG_QUEUE", cast=bool)


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
