from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    env: Literal["dev", "prod"] = "prod"

    cors_origins: list[str]
    cors_methods: list[str]


@lru_cache
def get_settings() -> Settings:
    return Settings()
