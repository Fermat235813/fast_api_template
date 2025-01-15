"""models

Main model of application

In this file the basic models of database schema is defined.

Classification: Unclassified
Autor: Lothar Janssen
"""

# adding here for generating models
from app.db.core_table import Base
from app.auth.models import Account

import datetime
import typing
import pydantic

from app.utils import format_datetime_into_iso_format
from app.utils import format_dict_key_to_camel_case


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