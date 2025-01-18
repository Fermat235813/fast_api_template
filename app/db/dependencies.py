"""Dependencies

Class which defines dependencies out of this package

functions:

    * get_config - get config

Classification: Unclassified
Autor: Lothar Janssen
"""
from app.config.config import AbstractSettings
from app.config.service import get_settings

def get_config() -> AbstractSettings:
    """
    Method to get current settings.
    :return: AbstractSettings current settings
    """
    return get_settings()