from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.

    Values are loaded from:
    1. Environment variables
    2. .env file
    3. Default values
    """

    app_name: str = "OpenCampus AI Framework"
    app_version: str = "0.1.0"
    environment: str = "development"

    log_level: str = "INFO"

    database_url: str = (
        "postgresql+asyncpg://"
        "opencampus:"
        "opencampus@"
        "localhost:"
        "5432/"
        "opencampus"
    )

    redis_host: str = "localhost"
    redis_port: int = 6380

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Cached application settings instance.
    """
    return Settings()


settings = get_settings()
print(settings.database_url)
