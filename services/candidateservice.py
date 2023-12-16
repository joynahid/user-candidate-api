from models import CandidateModel, UpdateCandidateModel, CandidateListModel
from models.candidate import QueryCandidateModel
from repositories import CandidateRepo


class CandidateService:
    def __init__(self, candidate_repo: CandidateRepo) -> None:
        self.candidate_repo = candidate_repo

    def create_candidate(self, candidate: CandidateModel) -> CandidateModel:
        """Create a new candidate."""
        candidate_dict = candidate.model_dump(by_alias=True, exclude=["id"])
        _id = self.candidate_repo.create(candidate_dict)
        new_candidate = self.candidate_repo.find_one(_id)
        return CandidateModel(**new_candidate)

    def update_candidate(
        self, id: str, updated_candidate: UpdateCandidateModel
    ) -> CandidateModel:
        """Update a candidate's information in the candidate repository"""
        updated_candidate_dict = updated_candidate.model_dump(by_alias=True)
        self.candidate_repo.update_one(id, updated_candidate_dict)
        updated_candidate = self.candidate_repo.find_one(id)
        return CandidateModel(**updated_candidate)

    def delete_candidate(self, candidate_id: str):
        """Delete a candidate from the db"""
        self.candidate_repo.delete_one(candidate_id)
        return True

    def get_candidate(self, candidate_id: str):
        """Retrieve a candidate from the db"""
        candidate = self.candidate_repo.find_one(candidate_id)
        return CandidateModel(**candidate)

    def get_all_candidates(self) -> CandidateListModel:
        """Retrieve all candidates and return the list"""
        candidates = self.candidate_repo.find()
        return CandidateListModel(candidates=candidates)

    def global_search_candiates(self, search_key: str) -> CandidateListModel:
        candidates = self.candidate_repo.search_all_fields(search_key)
        return CandidateListModel(candidates=candidates)

    def generate_report(self):
        pass
