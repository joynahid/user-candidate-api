from typing import Optional
import uuid
from pydantic import BaseModel, Field


class CandidateModel(BaseModel):
    """Represents a candidate profile"""

    id: Optional[str] = Field(alias="_id", default=None)
    UUID: Optional[str] = Field(default_factory=uuid.uuid4)
    first_name: str
    last_name: str
    email: str
    career_level: str   # ex: Junior, Senior, Mid Level…
    job_major: str      # ex: Computer Science, Computer Information Systems,...
    years_of_experience: int
    degree_type: str    # ex: Bachelor, Master, High School,...
    skills: list[str]
    nationality: str
    city: str
    salary: float
    gender: str         # should be a list of literals: [“Male”, “Female”, “Not Specified”]
