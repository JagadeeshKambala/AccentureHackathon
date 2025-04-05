from pydantic import BaseModel

class ResumeUploadRequest(BaseModel):
    text: str
    job_id: int

class ResumeExtractedData(BaseModel):
    name: str
    email: str
    phone: str | None = None
    skills: str
    experience: str
    education: str
    certifications: str | None = None
