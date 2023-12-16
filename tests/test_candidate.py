import unittest
from fastapi.testclient import TestClient
from config import db, get_database
from main import app
from models import CandidateModel


class TestCandidate(unittest.TestCase):
    def setUp(self):
        db.init_db(
            "mongodb://nahidtest:nahidpasswordtest@localhost:89/?retryWrites=true&w=majority"
        )
        self.db = get_database()
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

        for i in range(5):
            response = self.client.post("/candidate", json=new_candidate)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["id"])

    def test_update_candidate(self):
        candidates = self.db.get_collection('candidates').find()
        test_candidate = list(candidates)[0]

        update_candidate = dict(
            first_name="John",
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

        response = self.client.put(f"/candidate/{str(test_candidate['_id'])}", json=update_candidate)
        self.assertEqual(response.status_code, 200)

    def test_view_candidate(self):
        candidates = self.db.get_collection('candidates').find()
        test_candidate = list(candidates)[0]

        response = self.client.get(f"/candidate/{str(test_candidate['_id'])}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], str(test_candidate['_id']))

    def test_get_all_candidates(self):
        response = self.client.get("/all-candidates")
        self.assertEqual(response.status_code, 200)

    def test_zdelete_candidate(self):
        candidates = self.db.get_collection('candidates').find()
        test_candidate = list(candidates)[0]

        response = self.client.delete(f"/candidate/{str(test_candidate['_id'])}")
        self.assertEqual(response.status_code, 200)

    def test_candidate_model(self):
        user = CandidateModel(
            first_name="Nahid",
            last_name="Hasan",
            email="xyz@nahidhq.com",
            UUID="uuidfiswdghf",
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

    def tearDown(self) -> None:
        super().tearDown()
        # self.db.drop_collection('candidates')
        self.db.client.close()

if __name__ == "__main__":
    unittest.main()
