from typing import Optional
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

    def search_all_fields(self, query: str):
        search_qry = {
            "$or": [
                {"first_name": {"$regex": query, "$options": "i"}},
                {"last_name": {"$regex": query, "$options": "i"}},
                {"email": {"$regex": query, "$options": "i"}},
                {"career_level": {"$regex": query, "$options": "i"}},
                {"job_major": {"$regex": query, "$options": "i"}},
                {"years_of_experience": {"$regex": query, "$options": "i"}},
                {"degree_type": {"$regex": query, "$options": "i"}},
                {"skills": {"$regex": query, "$options": "i"}},
                {"nationality": {"$regex": query, "$options": "i"}},
                {"city": {"$regex": query, "$options": "i"}},
                {"salary": {"$regex": query, "$options": "i"}},
                {"gender": {"$regex": query, "$options": "i"}},
            ]
        }

        return list(super().find(search_qry))
