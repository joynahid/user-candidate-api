from functools import lru_cache
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str
    app_name: str = "UserCandidateAPI"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def read_settings():
    return Settings()
