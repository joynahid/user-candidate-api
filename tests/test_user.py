import unittest
from fastapi.testclient import TestClient
from main import app
from models import UserModel

class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_user_model(self):
        user = UserModel(first_name='Nahid', last_name='Hasan', email='xyz@nahidhq.com', UUID='uuidfiswdghf', _id="90")
        self.assertIsInstance(user, UserModel)

if __name__ == "__main__":
    unittest.main()
