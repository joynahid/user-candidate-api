import unittest
from fastapi.testclient import TestClient
from config import db, get_database
from main import app
from repositories import CandidateRepo, UserRepo
from services import CandidateService, UserService


class TestCandidateService(unittest.TestCase):
    def setUp(self):
        db.init_db(
            "mongodb://nahidtest:nahidpasswordtest@localhost:89/?retryWrites=true&w=majority"
        )
        self.db = get_database()
        self.client = TestClient(app)

    def test_user_service(self):
        service = UserService(UserRepo(self.db))
        self.assertIsInstance(service, UserService)


if __name__ == "__main__":
    unittest.main()
