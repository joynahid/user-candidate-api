from typing import Optional
import uuid
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    """Represents a user profile"""

    id: Optional[str] = Field(alias="_id", default=None)
    UUID: Optional[str] = Field(default_factory=uuid.uuid4)
    first_name: str
    last_name: str
    email: str
