import unittest
from fastapi.testclient import TestClient
from main import app
from models import UserModel


class TestCandidateService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_user(self):
        new_user = dict(
            first_name="John",
            last_name="Kabir",
            email="johnk@nahidhq.com",
        )

        response = self.client.post("/user", json=new_user)
        self.assertEqual(response.status_code, 201, 'Status code mismatched')

    def test_user_model(self):
        user = UserModel(
            first_name="Nahid",
            last_name="Hasan",
            email="xyz@nahidhq.com",
            UUID="uuidfiswdghf",
            _id="90",
        )
        self.assertIsInstance(user, UserModel)


if __name__ == "__main__":
    unittest.main()
