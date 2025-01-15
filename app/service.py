"""BaseCRUDRepository

Here the gen eric model for CRUD-Repositories is defined

Classification: Unclassified
Autor: Lothar Janssen
"""
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession


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
