from app.config.core_settings import CoreSettings
from app.config.environment import Environment


class StageSettings(CoreSettings):
    """
    StageSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
