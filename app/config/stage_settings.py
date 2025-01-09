from app.config.abstract_settings import AbstractSettings
from app.config.environment import Environment


class StageSettings(AbstractSettings):
    """
    StageSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
