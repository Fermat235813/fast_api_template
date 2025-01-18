"""events

Here database connection is managed by events

functions:

    * inspect_db_server_on_connection - event for init database connection
    * inspect_db_server_on_close - event for closing database connection
    * initialize_db_tables -  init tables of database
    * initialize_db_connection - init database tables
    * dispose_db_connection - close database connection

Classification: Unclassified
Autor: Lothar Janssen
"""
from sqlalchemy import event
from sqlalchemy.dialects.postgresql.asyncpg import AsyncAdapt_asyncpg_connection
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.pool.base import _ConnectionRecord

from app.db.service import async_db
from app.models import Base



@event.listens_for(target=async_db.async_engine.sync_engine, identifier="connect")
def inspect_db_server_on_connection(
    db_api_connection: AsyncAdapt_asyncpg_connection, connection_record: _ConnectionRecord
) -> None:
    """
    event for init database connection
    :param db_api_connection: AsyncAdapt_asyncpg_connection
    :param connection_record: _ConnectionRecord
    :return: nothing
    """
    pass


@event.listens_for(target=async_db.async_engine.sync_engine, identifier="close")
def inspect_db_server_on_close(
    db_api_connection: AsyncAdapt_asyncpg_connection, connection_record: _ConnectionRecord
) -> None:
    """
    event for closing database connection
    :param db_api_connection: AsyncAdapt_asyncpg_connection
    :param connection_record: _ConnectionRecord
    :return: nothing
    """
    pass

async def initialize_db_tables(connection: AsyncConnection) -> None:
    """
    init tables of database
    :param connection: AsyncConnection connection
    :return: nothing
    """
    await connection.run_sync(Base.metadata.drop_all)
    await connection.run_sync(Base.metadata.create_all)


async def initialize_db_connection() -> None:
    """
    init database tables
    :return: noting
    """
    async with async_db.async_engine.begin() as connection:
        await initialize_db_tables(connection=connection)


async def dispose_db_connection() -> None:
    """
    close database connection
    :return: nothing
    """
    await async_db.async_engine.dispose()

