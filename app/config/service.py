"""services
This is to provide to current configuration.

classes:

    * ProdSettings - Production settings
    * DevSettings - Development settings
    * StageSettings - Testing settings

Classification: Unclassified
Autor: Lothar Janssen
"""
from functools import lru_cache
import decouple
from app.config.config import AbstractSettings
from app.config.utils import Environment



class ProdSettings(AbstractSettings):
    """
    ProdSettings which overrides the default settings.
    """
    SUMMARY: str | None = "Production Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION


class StageSettings(AbstractSettings):
    """
    StageSettings which overrides the default settings.
    """
    SUMMARY: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING



class DevSettings(AbstractSettings):
    """
    DevSettings which overrides the default settings.
    """
    SUMMARY: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT


class ConfigFactory:
    """
    Factory for getting the specific configuration
    """
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> AbstractSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return DevSettings()
        elif self.environment == Environment.STAGING.value:
            return StageSettings()
        return ProdSettings()


@lru_cache
def get_settings() -> AbstractSettings:
    """
    Set LRU-Cache, so the most likely environment will get.
    :return: ConfigFactory instance
    """
    return ConfigFactory(environment=decouple.config("ENVIRONMENT", default="DEV", cast=str))()


settings: AbstractSettings = get_settings()