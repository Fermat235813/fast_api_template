from app.config.abstract_settings import AbstractSettings
from app.config.environment import Environment


class ProdSettings(AbstractSettings):
    """
    ProdSettings which overrides the default settings.
    """

    SUMMARY: str | None = "Production Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION
