from pydantic import BaseModel

class JobDescriptionRequest(BaseModel):
    text: str

class JobSummaryResponse(BaseModel):
    job_id: int
    summary: dict
