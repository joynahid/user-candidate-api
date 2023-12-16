from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, FastAPI
from config import db
from config import get_database, read_settings, Settings, close_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Do Stuffs
    settings: Settings = read_settings()
    db.init_db(settings.mongodb_url)

    yield

    # Clean up resources
    close_database()
