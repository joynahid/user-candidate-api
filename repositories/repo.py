from abc import ABC


class IRepo(ABC):
    def create(self):
        """Create an entry"""
        ...

    def find_one(self):
        """Find unique entry by id"""
        ...

    def find_all(self):
        """Find all entries"""
        ...

    def update_one(self):
        """Update an entry"""
        ...

    def delete_one(self):
        """Delete an entry"""
        ...

class BaseRepo(IRepo):
    def create(self):
        pass

    def find_one(self):
        pass

    def find_all(self):
        pass

    def update_one(self):
        pass

    def delete_one(self):
        pass
