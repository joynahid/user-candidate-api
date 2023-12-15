from abc import ABC, abstractmethod
from typing import Optional
from bson import ObjectId
from pymongo.database import Database


class IRepo(ABC):
    @abstractmethod
    def create(self):
        """Create an entry"""
        ...

    @abstractmethod
    def find_one(self):
        """Find unique entry by id"""
        ...

    @abstractmethod
    def find(self):
        """Find all entries"""
        ...

    @abstractmethod
    def update_one(self):
        """Update an entry"""
        ...

    @abstractmethod
    def delete_one(self):
        """Delete an entry"""
        ...


class BaseRepo(IRepo):
    def __init__(self, db: Database, collection_name: str) -> None:
        super().__init__()
        self.db = db
        self.collection = self.db.get_collection(collection_name)

    def create(self, data: dict):
        return self.collection.insert_one(data).inserted_id

    def find_one(self, id: str):
        return self.collection.find_one({"_id": ObjectId(id)})

    def find(self, data: Optional[dict]):
        if data is None:
            return self.collection.find()
        return self.collection.find(data)

    def update_one(self, id: str, data: dict):
        return self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})

    def delete_one(self, id: str):
        return self.collection.delete_one({"_id": ObjectId(id)})
