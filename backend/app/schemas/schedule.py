from pydantic import BaseModel

class InterviewScheduleRequest(BaseModel):
    candidate_name: str
    email: str
    job_title: str

class InterviewEmailResponse(BaseModel):
    email_to: str
    email_body: str
