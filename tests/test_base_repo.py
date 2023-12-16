import unittest
from fastapi.testclient import TestClient
from main import app
from models import UserModel
from config import db, get_database
from repositories import BaseRepo
from . import MONGODB_TEST_URL


class TestBaseRepo(unittest.TestCase):
    def setUp(self):
        db.init_db(
            MONGODB_TEST_URL
        )
        self.db = get_database()
        self.client = TestClient(app)

    def test_repo(self):
        base_repo = BaseRepo(self.db, "somecollection")
        self.assertIsInstance(base_repo, BaseRepo)

        new_data = base_repo.create({"hello": "world", "1": 2})
        data = base_repo.find_one(str(new_data))
        self.assertEqual(data["hello"], "world")
        delete_res = base_repo.delete_one(str(new_data))
        self.assertEqual(delete_res.deleted_count, 1)


if __name__ == "__main__":
    unittest.main()
