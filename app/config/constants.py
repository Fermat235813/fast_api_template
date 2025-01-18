"""constants
Here constants for http exception are defined

    * define_postgres_url
    * define_async_postgres_url

Classification: Unclassified
Autor: Lothar Janssen
"""
from pydantic import PostgresDsn
from app.config.service import settings


def define_postgres_url() -> PostgresDsn:
    """
    Define a PostgresDsn from the environment variables.
    :return: url string
    """
    return PostgresDsn(
        url=f"{settings.DB_POSTGRES_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@"
        f"{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}",
    )


def define_async_postgres_url() -> str:
    """
    Define a PostgresDsn from the environment variables.
    :return: url string
    """
    return (
        f"{settings.DB_POSTGRES_ASYNC_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@"
        f"{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}"
    )