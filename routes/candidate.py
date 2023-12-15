from typing import Optional
from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse

from models import CandidateModel, UpdateCandidateModel, CandidateListModel

router = APIRouter()


@router.post("/candidate")
def create_candidate(candidate: CandidateModel):
    """Create a new candidate entry to the candidates collection"""

    return JSONResponse(
        content=candidate.model_dump_json(), status_code=status.HTTP_201_CREATED
    )


@router.put("/candidate/{id}")
def update_candidate(id: str, candidate: UpdateCandidateModel) -> UpdateCandidateModel:
    """Update a candidate entry"""
    return JSONResponse(
        content=candidate.model_dump_json(), status_code=status.HTTP_200_OK
    )


@router.get("/candidate/{id}")
def view_candidate(id: str):
    """Return a candidate"""
    candidate = CandidateModel()
    return JSONResponse(
        content=candidate.model_dump_json(), status_code=status.HTTP_200_OK
    )


@router.delete("/candidate/{id}")
def delete_candidate(id: str):
    """Delete a candidate from the candidates collection"""
    return Response(status_code=status.HTTP_200_OK)


@router.get("/all-candidates")
def get_all_candidates(
    skip: Optional[int] = 0, limit: int = 50, search: Optional[str] = None
):
    """List all candidates from the candidates collection"""
    candidates = CandidateListModel()

    return JSONResponse(
        content=candidates.model_dump_json(), status_code=status.HTTP_200_OK
    )
