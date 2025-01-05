from pydantic import PostgresDsn

from app.config.config_factory import get_settings


def define_postgres_url() -> PostgresDsn:
    """
    Define a PostgresDsn from the environment variables.
    """
    settings = get_settings()
    return PostgresDsn(
        url=f"{settings.DB_POSTGRES_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@"
        f"{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}",
    )


def define_async_postgres_url() -> str:
    """
    Define connection-url from the environment variables.
    """
    settings = get_settings()
    return (
        f"{settings.DB_POSTGRES_ASYNC_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@"
        f"{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}"
    )
