from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from models.user import UserModel


router = APIRouter()


@router.post("/user")
def create_user(user: UserModel):
    """Create a new user entry to the users collection"""

    user = UserModel()

    return JSONResponse(
        content=user.model_dump(), status_code=status.HTTP_201_CREATED
    )
