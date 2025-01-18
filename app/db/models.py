"""DBTable

Base class which defined every table of database

"""
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class DBTable(DeclarativeBase):
    """
    Base class which defined every table of database
    """
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()  # type: ignore


Base: type[DeclarativeBase] = DBTable
