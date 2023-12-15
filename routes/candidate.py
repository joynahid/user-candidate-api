import csv
import io
from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse
from config import get_database, read_settings

from models import CandidateModel, UpdateCandidateModel, CandidateListModel
from repositories import CandidateRepo
from services import CandidateService

router = APIRouter()


@router.post("/candidate")
def create_candidate(candidate: CandidateModel, db = Depends(get_database)):
    """Create a new candidate entry to the candidates collection"""

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)

    new_candidate = candidate_service.create_candidate(candidate)

    return JSONResponse(
        content=new_candidate.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.put("/candidate/{id}")
def update_candidate(id: str, candidate: UpdateCandidateModel, db = Depends(get_database)) -> UpdateCandidateModel:
    """Update a candidate entry"""
    return JSONResponse(
        content=candidate.model_dump(), status_code=status.HTTP_200_OK
    )


@router.get("/candidate/{id}")
def view_candidate(id: str):
    """Return a candidate"""
    candidate = CandidateModel()
    return JSONResponse(
        content=candidate.model_dump(), status_code=status.HTTP_200_OK
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
        content=candidates.model_dump(), status_code=status.HTTP_200_OK
    )


@router.get("/generate-report")
def generate_report(
    skip: Optional[int] = 0, limit: int = 50, search: Optional[str] = None
):
    """
    Generate a report of all candidates' information in a CSV
    file, taking into account if you have many candidates in the database.
    """
    
    candidates = []

    stream = io.StringIO()
    writer = csv.writer(stream)

    # Write CSV headers
    writer.writerow(["Name", "Email", "Qualifications"])  # Replace with actual candidate fields

    # Write candidate data
    for candidate in candidates:
        writer.writerow([candidate.name, candidate.email, candidate.qualifications])  # Replace with actual data fields

    response = Response(stream.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=report.csv"
    return response
