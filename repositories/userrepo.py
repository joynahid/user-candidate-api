from pymongo.database import Database

from .repo import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self, db: Database, collection_name: str = "users") -> None:
        """Initialization of UserRepo instance

        Args:
            db (Database): A pymongo Database instance
            collection_name (str, optional): Name of the collection. Defaults to "users".
        """
        super().__init__(db, collection_name)
        self.db = db
        self.collection = self.db.get_collection(collection_name)
