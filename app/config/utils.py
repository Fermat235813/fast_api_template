"""utils

Class to define configuration.

classes:

    * Environment - environment variables

Classification: Unclassified
Autor: Lothar Janssen
"""
import enum

class Environment(str, enum.Enum):
    """
    Environment class to define environment variables.
    """
    PRODUCTION: str = "PROD"  # type: ignore
    DEVELOPMENT: str = "DEV"  # type: ignore
    STAGING: str = "STAGE"  # type: ignore
