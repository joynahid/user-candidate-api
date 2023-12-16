import csv
import io
from typing import Optional, Union
from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse
from config import get_database

from models import CandidateModel, UpdateCandidateModel, CandidateListModel
from models.candidate import QueryCandidateModel
from models.shared import PyObjectId
from repositories import CandidateRepo
from services import CandidateService

router = APIRouter()


@router.post("/candidate", response_model=CandidateModel)
def create_candidate(candidate: CandidateModel, db=Depends(get_database)):
    """Create a new candidate entry to the candidates collection"""

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)
    new_candidate = candidate_service.create_candidate(candidate)

    return JSONResponse(
        content=new_candidate.model_dump(by_alias=False),
        status_code=status.HTTP_201_CREATED,
    )


@router.put("/candidate/{id}", response_model=CandidateModel)
def update_candidate(
    id: PyObjectId, candidate: UpdateCandidateModel, db=Depends(get_database)
):
    """Update a candidate entry"""

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)
    updated_candidate = candidate_service.update_candidate(id, candidate)

    return JSONResponse(
        content=updated_candidate.model_dump(by_alias=False),
        status_code=status.HTTP_200_OK,
    )


@router.get("/candidate/{id}", response_model=CandidateModel)
def view_candidate(id: PyObjectId, db=Depends(get_database)):
    """Return a candidate"""
    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)
    candidate = candidate_service.get_candidate(id)

    return JSONResponse(
        content=candidate.model_dump(by_alias=False), status_code=status.HTTP_200_OK
    )


@router.delete("/candidate/{id}")
def delete_candidate(id: PyObjectId, db=Depends(get_database)):
    """Delete a candidate from the candidates collection"""

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)
    candidate_service.delete_candidate(id)

    return Response(status_code=status.HTTP_200_OK)


@router.get("/all-candidates", response_model=CandidateListModel)
def get_all_candidates(
    search: Optional[str] = None,
    db=Depends(get_database),
):
    """List all candidates from the candidates collection"""

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)

    candidate_list = CandidateListModel(candidates=[])

    if search is None:
        candidate_list = candidate_service.get_all_candidates()
    elif isinstance(search, str):
        candidate_list = candidate_service.global_search_candiates(search)

    return JSONResponse(
        content=candidate_list.model_dump(by_alias=False),
        status_code=status.HTTP_200_OK,
    )


@router.get("/generate-report")
def generate_report(
    db=Depends(get_database),
):
    """
    Generate a report of all candidates' information in a CSV
    file, taking into account if you have many candidates in the database.
    """

    candidate_repo = CandidateRepo(db)
    candidate_service = CandidateService(candidate_repo)

    candidate_list = candidate_service.get_all_candidates()

    stream = io.StringIO()
    writer = csv.writer(stream)

    # Write CSV headers
    writer.writerow(
        [
            "Name",
            "Email",
            "Career Level",
            "Job Major",
            "Years of Experience",
            "Degree Type",
            "Skills",
            "Nationality",
            "City",
            "Salary",
            "Gender",
        ]
    )  # Replace with actual candidate fields

    # Write candidate data
    for candidate in candidate_list.candidates:
        writer.writerow(
            [
                candidate.name,
                candidate.email,
                candidate.career_level,
                candidate.job_major,
                candidate.years_of_experience,
                candidate.degree_type,
                ", ".join(candidate.skills),
                candidate.nationality,
                candidate.city,
                candidate.salary,
                candidate.gender,
            ]
        )  # Replace with actual data fields

    response = Response(stream.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=report.csv"
    return response
