from models import UserModel
from repositories import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    def create_user(self, user: UserModel) -> UserModel:
        return user
