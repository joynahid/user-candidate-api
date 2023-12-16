import unittest
from fastapi.testclient import TestClient
from main import app
from models import UserModel
from config import db, get_database
from repositories import CandidateRepo
from . import MONGODB_TEST_URL


class TestCandidateRepo(unittest.TestCase):
    def setUp(self):
        db.init_db(
            MONGODB_TEST_URL
        )
        self.db = get_database()
        self.client = TestClient(app)

    def test_repo(self):
        candidate_repo = CandidateRepo(self.db)
        self.assertIsInstance(candidate_repo, CandidateRepo)


if __name__ == "__main__":
    unittest.main()
