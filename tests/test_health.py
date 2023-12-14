import unittest
from fastapi.testclient import TestClient
from main import app

class TestHealthAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
