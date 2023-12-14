from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: str = Field(alias="_id")
    first_name: str
    last_name: str
    email: str
    UUID: str
