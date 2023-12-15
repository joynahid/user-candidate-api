from models import CandidateModel, UpdateCandidateModel, CandidateListModel
from repositories import CandidateRepo


class CandidateService:
    def __init__(self, candidate_repo: CandidateRepo) -> None:
        self.candidate_repo = candidate_repo

    def create_candidate(self, candidate: CandidateModel) -> CandidateModel:
        return candidate

    def update_candidate(
        self, updated_candidate: UpdateCandidateModel
    ) -> CandidateModel:
        return updated_candidate

    def delete_candidate(self, candidate_id: str):
        return True

    def get_candidate(self, candidate_id: str):
        return None

    def get_all_candidates(self) -> CandidateListModel:
        return CandidateListModel()

    def search_candidates_by_params(self):
        pass

    def global_search_candiates(self):
        pass
