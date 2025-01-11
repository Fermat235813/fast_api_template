import pydantic
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.pool import Pool, AsyncAdaptedQueuePool

from app.config.config_factory import settings
from app.config.utils import define_async_postgres_url, define_postgres_url


class AsyncDatabase:
    """
    Class representing an asynchronous database connection.
    """

    def __init__(self) -> None:
        self.postgres_uri: pydantic.PostgresDsn = define_postgres_url()
        self.async_engine: AsyncEngine = create_async_engine(
            url=define_async_postgres_url(),
            echo=settings.IS_DB_ECHO_LOG,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_POOL_OVERFLOW,
            poolclass=AsyncAdaptedQueuePool,
        )
        self.async_session: AsyncSession = AsyncSession(bind=self.async_engine)
        self.pool: Pool = self.async_engine.pool


async_db: AsyncDatabase = AsyncDatabase()
