import unittest
from fastapi.testclient import TestClient
from config import db, get_database
from main import app
from models.user import UserModel
from repositories import CandidateRepo, UserRepo
from services import CandidateService, UserService
from . import MONGODB_TEST_URL


class TestCandidateService(unittest.TestCase):
    def setUp(self):
        db.init_db(MONGODB_TEST_URL)
        self.db = get_database()
        self.client = TestClient(app)
        self.service = UserService(UserRepo(self.db), "mysecret")

    def test_user_service(self):
        self.assertIsInstance(self.service, UserService)

    def test_authentication(self):
        user = UserModel(
            email="n@n.com",
            password=self.service.hash_password("iamnobody"),
            first_name="nahid",
            last_name="hasan",
        )

        encoded_jwt = self.service.create_access_token(user)
        self.assertTrue(encoded_jwt)

        self.assertTrue(self.service.verify_password("iamnobody", user.password))
        self.assertFalse(self.service.verify_password("iamnobodw", user.password))


if __name__ == "__main__":
    unittest.main()
