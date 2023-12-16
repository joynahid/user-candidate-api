from dataclasses import dataclass, field
from datetime import datetime, timedelta
import hashlib
from typing import Optional, Union

import jwt
from config import settings
from models import UserModel
from repositories import UserRepo


@dataclass
class UserService:
    user_repo: UserRepo
    jwt_secret: str = field(repr=False)
    jwt_algorithm: str = field(default="HS256")

    def create_user(self, user: UserModel) -> UserModel:
        """Create a new user"""

        users = list(self.user_repo.find({"email": user.email}))

        if len(users) == 1:
            raise ValueError(f"User already exists with the email {user.email}")

        user_dict = user.model_dump(exclude=["id"])
        _id = self.user_repo.create(user_dict)
        new_user = self.user_repo.find_one(_id)
        return UserModel(**new_user)

    def authenticate_user(self, email: str, password: str) -> Union[UserModel, None]:
        users = list(self.user_repo.find({"email": email}))

        if len(users) != 1:
            raise ValueError(f"User not found")

        user = users[0]

        if user and self.verify_password(password, user["password"]):
            return UserModel(**user)
        return None

    def decode_access_token(self, token: str) -> UserModel:
        decoded_jwt = jwt.decode(
            token, self.jwt_secret, algorithms=[self.jwt_algorithm]
        )
        user = self.user_repo.find_one(decoded_jwt["sub"])
        return UserModel(**user)

    def create_access_token(self, user: UserModel):
        to_encode = {
            "iss": user.email,
            "sub": str(user.id),
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=1),
        }

        encoded_jwt = jwt.encode(
            to_encode, self.jwt_secret, algorithm=self.jwt_algorithm
        )
        return encoded_jwt

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return UserService.hash_password(plain_password) == hashed_password
