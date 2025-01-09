from app.config.abstract_settings import AbstractSettings
from app.config.environment import Environment


class DevSettings(AbstractSettings):
    """
    DevSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
