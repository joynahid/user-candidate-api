from typing import Annotated, Optional
import uuid
from pydantic import BaseModel, BeforeValidator, Field


class UserModel(BaseModel):
    """Represents a user profile"""

    id: Optional[Annotated[str, BeforeValidator(str)]] = Field(
        alias="_id", default=None
    )
    UUID: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    email: str
