from app.config.core_settings import CoreSettings
from app.config.environment import Environment


class DevSettings(CoreSettings):
    """
    DevSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
