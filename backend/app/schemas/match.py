from pydantic import BaseModel

class MatchRequest(BaseModel):
    resume_text: str
    job_id: int

class MatchResult(BaseModel):
    match_score: float
    explanation: str
    shortlisted: bool
