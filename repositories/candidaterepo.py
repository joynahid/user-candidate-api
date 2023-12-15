from pymongo.database import Database
from models import QueryCandidateModel, UpdateCandidateModel

from .repo import BaseRepo


class CandidateRepo(BaseRepo):
    def __init__(self, db: Database, collection_name: str = "candidates") -> None:
        """Initialization of UserRepo instance

        Args:
            db (Database): A pymongo Database instance
            collection_name (str, optional): Name of the collection. Defaults to "candidates".
        """
        super().__init__(db, collection_name)
        self.db = db
        self.collection = self.db.get_collection(collection_name)
