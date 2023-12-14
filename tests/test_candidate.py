import unittest
from fastapi.testclient import TestClient
from main import app
from models import CandidateModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_candidate_model(self):
        user = CandidateModel(
            first_name="Nahid",
            last_name="Hasan",
            email="xyz@nahidhq.com",
            UUID="uuidfiswdghf",
            _id="90",
            career_level="Junior",
            job_major="Computer Science",
            years_of_experience=5,
            degree_type="Bachelor",
            skills=["Python", "JS"],
            nationality="American",
            city="NY",
            salary=10000.50,
            gender="Male",
        )
        self.assertIsInstance(user, CandidateModel)


if __name__ == "__main__":
    unittest.main()
