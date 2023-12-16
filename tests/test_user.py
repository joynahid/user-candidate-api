import unittest
from fastapi.testclient import TestClient
from main import app
from models import UserModel
from config import db, get_database


class TestUser(unittest.TestCase):
    def setUp(self):
        db.init_db(
            "mongodb://nahidtest:nahidpasswordtest@localhost:89/?retryWrites=true&w=majority"
        )
        self.db = get_database()
        self.client = TestClient(app)

    def test_create_user(self):
        new_user = dict(
            first_name="John",
            last_name="Kabir",
            email="johnk@nahidhq.com",
        )

        response = self.client.post("/user", json=new_user)
        self.assertEqual(response.status_code, 201, 'Status code mismatched')
        self.assertTrue(response.json()['id'])


    def test_user_model(self):
        user = UserModel(
            first_name="Nahid",
            last_name="Hasan",
            email="xyz@nahidhq.com",
            UUID="uuidfiswdghf"
        )
        self.assertIsInstance(user, UserModel)



if __name__ == "__main__":
    unittest.main()
