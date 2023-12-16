import unittest
from fastapi.testclient import TestClient
from config import db, get_database
from main import app
from repositories import CandidateRepo
from services import CandidateService
from . import MONGODB_TEST_URL


class TestCandidateService(unittest.TestCase):
    def setUp(self):
        db.init_db(
            MONGODB_TEST_URL
        )
        self.db = get_database()
        self.client = TestClient(app)

    def test_candidate_service(self):
        service = CandidateService(candidate_repo=CandidateRepo(self.db))
        self.assertIsInstance(service, CandidateService)


if __name__ == "__main__":
    unittest.main()
