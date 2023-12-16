from models import UserModel
from repositories import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo) -> None:
        self.user_repo = user_repo

    def create_user(self, user: UserModel) -> UserModel:
        """Create a new user"""
        user_dict = user.model_dump(exclude=["id"])
        _id = self.user_repo.create(user_dict)
        new_user = self.user_repo.find_one(_id)
        return UserModel(**new_user)
