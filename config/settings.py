from functools import lru_cache
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "UserCandidateAPI"
    admin_email: str
    mongodb_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def read_settings():
    return Settings()
