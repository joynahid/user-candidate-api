from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from starlette.responses import JSONResponse
from config import get_database
from config import Settings
from config.settings import read_settings

from models.user import UserLoginModel, UserModel
from repositories import UserRepo
from .utils import Utils
from services import UserService


router = APIRouter()


@router.post("/user", response_model=UserModel)
def create_user(
    user: UserModel,
    db=Depends(get_database),
    settings: Settings = Depends(read_settings),
):
    """Create a new user entry to the users collection"""

    user_repo = UserRepo(db)
    user_service = UserService(user_repo, settings.jwt_secret, settings.jwt_algorithm)
    user.password = user_service.hash_password(user.password)
    new_user = user_service.create_user(user)

    return JSONResponse(
        content=new_user.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.post("/login")
async def login(
    login: UserLoginModel,
    db=Depends(get_database),
    settings: Settings = Depends(read_settings),
):
    user_repo = UserRepo(db)
    user_service = UserService(user_repo, settings.jwt_secret, settings.jwt_algorithm)
    user = user_service.authenticate_user(login.email, login.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Credentials",
        )

    access_token = user_service.create_access_token(user)
    response = JSONResponse(content={"access_token": access_token})
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response


@router.get(
    "/user",
    response_model=UserModel,
    openapi_extra={
        "security": {
            "cookieAuth": {"type": "apiKey", "in": "cookie", "name": "access_token"}
        }
    },
)
def get_current_user(
    user: Annotated[UserModel, Depends(Utils.auth_middleware)],
):
    """Get the current logged in user"""
    return JSONResponse(content=user.model_dump(by_alias=False))
