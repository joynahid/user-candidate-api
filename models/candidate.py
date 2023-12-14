from pydantic import BaseModel, Field


class CandidateModel(BaseModel):
    """Represents a candidate profile"""

    id: str = Field(alias="_id")
    UUID: str
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
