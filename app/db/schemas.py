"""logging

Schema for LogEntries

classes:

    * RequestLog - class for defining Request Log
    * ResponseLog - class for defining Response Log

Classification: Unclassified
Autor: Lothar Janssen
"""
import datetime
import typing
import pydantic
from app.db.utils import format_datetime_into_iso_format
from app.db.utils import format_dict_key_to_camel_case


class BaseSchemaModel(pydantic.BaseModel):
    """
    Base schema model for database schema
    """
    class Config(pydantic.BaseConfig):
        """
        Config model for database schema model
        """
        orm_mode: bool = True
        validate_assignment: bool = True
        allow_population_by_field_name: bool = True
        json_encoders: dict = {datetime.datetime: format_datetime_into_iso_format}
        alias_generator: typing.Any = format_dict_key_to_camel_case