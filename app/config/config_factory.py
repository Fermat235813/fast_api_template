from functools import lru_cache

import decouple

from app.config.core_settings import CoreSettings
from app.config.dev_settings import DevSettings
from app.config.environment import Environment
from app.config.prod_settings import ProdSettings
from app.config.stage_settings import StageSettings


class ConfigFactory:
    """
    Factory for getting the specific configuration
    """

    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> CoreSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return DevSettings()
        elif self.environment == Environment.STAGING.value:
            return StageSettings()
        return ProdSettings()


@lru_cache
def get_settings() -> CoreSettings:
    """
    Set LRU-Cache, so the most likely environment will get.
    """
    return ConfigFactory(
        environment=decouple.config("ENVIRONMENT", default="DEV", cast=str)
    )()


settings: CoreSettings = get_settings()
