"""AsyncDatabase

Here general database service

classes:

    * AsyncDatabase - asynchron connection to database
    * BaseCRUDRepository - base CRUD repository

Classification: Unclassified
Autor: Lothar Janssen
"""
import pydantic
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.pool import Pool, AsyncAdaptedQueuePool
from app.config.constants import define_async_postgres_url, define_postgres_url
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession
from app.db.dependencies import get_config


class AsyncDatabase:
    """
    Class representing an asynchronous database connection.
    """

    def __init__(self) -> None:
        self.postgres_uri: pydantic.PostgresDsn = define_postgres_url()
        self.async_engine: AsyncEngine = create_async_engine(
            url=define_async_postgres_url(),
            echo=get_config().IS_DB_ECHO_LOG,
            pool_size=get_config().DB_POOL_SIZE,
            max_overflow=get_config().DB_POOL_OVERFLOW,
            poolclass=AsyncAdaptedQueuePool,
        )
        self.async_session: AsyncSession = AsyncSession(bind=self.async_engine)
        self.pool: Pool = self.async_engine.pool

async_db: AsyncDatabase = AsyncDatabase()


class BaseCRUDRepository:
    """
    BaseCRUDRepository
    """
    def __init__(self, async_session: SQLAlchemyAsyncSession) -> None:
        """
        function to call session
        :param async_session: async_session object
        """
        self.async_session = async_session