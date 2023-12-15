import unittest
from fastapi.testclient import TestClient
from main import app
from models import CandidateModel


class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_candidate(self):
        new_candidate = dict(
            first_name="Avoid",
            last_name="Rafa",
            email="avoidr@nahidhq.com",
            career_level="Junior",
            job_major="CS",
            years_of_experience=6,
            degree_type="BSc",
            skills=["Python", "C++"],
            nationality="Indian",
            city="Gujarat",
            salary=30000,
            gender="Male",
        )

        response = self.client.post("/candidate", json=new_candidate)
        self.assertEqual(response.status_code, 201)

    def test_update_candidate(self):
        update_candidate = dict(
            first_name="Avoid",
            last_name="Rafa",
            email="avoidr@nahidhq.com",
            career_level="Junior",
            job_major="CS",
            years_of_experience=6,
            degree_type="BSc",
            skills=["Python", "C++"],
            nationality="Indian",
            city="Gujarat",
            salary=30000,
            gender="Male",
        )

        response = self.client.put("/candidate/id2", json=update_candidate)
        self.assertEqual(response.status_code, 200)

    def test_delete_candidate(self):
        response = self.client.delete("/candidate/id2", params=dict(candidate_id="id1"))
        self.assertEqual(response.status_code, 200)

    def test_view_candidate(self):
        response = self.client.delete("/candidate/id2", params=dict(candidate_id="id1"))
        self.assertEqual(response.status_code, 200)

    def test_get_all_candidates(self):
        response = self.client.get("/all-candidates", params=dict(candidate_id="id1"))
        self.assertEqual(response.status_code, 200)

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
