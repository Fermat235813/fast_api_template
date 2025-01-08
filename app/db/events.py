from sqlalchemy.ext.asyncio import AsyncConnection

from app.db.database import async_db
from app.models import Base



async def initialize_db_tables(connection: AsyncConnection) -> None:

    await connection.run_sync(Base.metadata.drop_all)
    await connection.run_sync(Base.metadata.create_all)


async def initialize_db_connection() -> None:

    async with async_db.async_engine.begin() as connection:
        await initialize_db_tables(connection=connection)



async def dispose_db_connection() -> None:

    await async_db.async_engine.dispose()