from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from models.user import UserModel


router = APIRouter()


@router.post("/user")
def create_user(user: UserModel):
    """Create a new user entry to the users collection"""
    return JSONResponse(
        content=user.model_dump_json(), status_code=status.HTTP_201_CREATED
    )
