from functools import lru_cache
from typing import Annotated
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str
    app_name: str = "UserCandidateAPI"
    jwt_secret: str = "234678rtiewuygfjdsvc"
    jwt_algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def read_settings():
    return Settings()
