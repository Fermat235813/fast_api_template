from app.config.core_settings import CoreSettings
from app.config.environment import Environment


class ProdSettings(CoreSettings):
    """
    ProdSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Production Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION
