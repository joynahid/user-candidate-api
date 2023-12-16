from typing import Annotated, Optional
import uuid
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

from .shared import PyObjectId


class UserModel(BaseModel):
    """Represents a user profile"""

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    UUID: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    email: str
    password: str = Field(exclude=True, default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
                "password": "SuperSecretP4ss",
            }
        },
    
    )


class UserLoginModel(BaseModel):
    """User Model for logging in"""

    email: str
    password: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "email": "jdoe@example.com",
                "password": "SuperSecretP4ss",
            }
        },
    )
