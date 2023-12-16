from typing import Annotated
from fastapi import Depends, HTTPException, Request, status
import jwt
from config import get_database
from config.settings import read_settings
from models.user import UserModel

from repositories import UserRepo
from services import UserService


class Utils:
    @staticmethod
    def auth_middleware(request: Request, db=Depends(get_database)):
        token = request.cookies.get("access_token")
        settings = read_settings()
        if not token:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )

        try:
            user_repo = UserRepo(db)
            user_service = UserService(
                user_repo, settings.jwt_secret, settings.jwt_algorithm
            )
            request.state.user = user_service.decode_access_token(token)
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )

        return request.state.user
