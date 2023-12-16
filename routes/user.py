from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse
from config import get_database

from models.user import UserModel
from repositories import UserRepo
from services import UserService


router = APIRouter()


@router.post("/user", response_model=UserModel)
def create_user(user: UserModel, db=Depends(get_database)):
    """Create a new user entry to the users collection"""

    user_repo = UserRepo(db)
    user_service = UserService(user_repo)

    new_user = user_service.create_user(user)

    return JSONResponse(
        content=new_user.model_dump(), status_code=status.HTTP_201_CREATED
    )
