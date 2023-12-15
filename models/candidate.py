from typing import List, Optional
import uuid
from pydantic import BaseModel, ConfigDict, Field


class CandidateModel(BaseModel):
    """Represents a candidate profile"""

    id: Optional[str] = Field(alias="_id", default=None)
    UUID: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    first_name: str
    last_name: str
    email: str
    career_level: str  # ex: Junior, Senior, Mid Level…
    job_major: str  # ex: Computer Science, Computer Information Systems,...
    years_of_experience: int
    degree_type: str  # ex: Bachelor, Master, High School,...
    skills: list[str]
    nationality: str
    city: str
    salary: float
    gender: str  # should be a list of literals: [“Male”, “Female”, “Not Specified”]

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
                "career_level": "Senior",
                "job_major": "Computer Science",
                "years_of_experience": 10,
                "degree_type": "Master",
                "skills": ["Python", "C#"],
                "nationality": "American",
                "city": "NY",
                "salary": 50000,
                "gender": "Male",
            }
        },
    )


class UpdateCandidateModel(BaseModel):
    """Represents a candidate profile for updating"""

    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    career_level: Optional[str] = Field(default=None)  # ex: Junior, Senior, Mid Level…
    job_major: Optional[str] = Field(
        default=None
    )  # ex: Computer Science, Computer Information Systems,...
    years_of_experience: Optional[int] = Field(default=None)
    degree_type: Optional[str] = Field(
        default=None
    )  # ex: Bachelor, Master, High School,...
    skills: Optional[List[str]] = Field(default=None)
    nationality: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    salary: Optional[float] = Field(default=None)
    gender: Optional[str] = Field(
        default=None
    )  # should be a list of literals: [“Male”, “Female”, “Not Specified”]

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
                "career_level": "Senior",
                "job_major": "Computer Science",
                "years_of_experience": 10,
                "degree_type": "Master",
                "skills": ["Python", "C#"],
                "nationality": "American",
                "city": "NY",
                "salary": 50000,
                "gender": "Male",
            }
        },
    )


class CandidateListModel(BaseModel):
    candidates: List[CandidateModel] = Field(default=[])
