from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import shutil

app = FastAPI()

# CORS setup for frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
job_descriptions = {}
resumes = {}
shortlisted = []

# Pydantic model for job description input
class JobDescriptionInput(BaseModel):
    text: str

@app.post("/api/upload-jd")
async def upload_jd(data: JobDescriptionInput):
    job_id = len(job_descriptions) + 1
    job_descriptions[job_id] = data.text
    return {"message": "Job description uploaded", "job_id": job_id}

@app.post("/api/upload-resume")
async def upload_resume(job_id: int = Form(...), file: UploadFile = File(...)):
    # Simulate file save
    filename = f"uploads/{file.filename}"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    match_score = 75  # Simulated score
    resumes[job_id] = {"filename": file.filename, "match_score": match_score}
    shortlisted.append({"job_id": job_id, "resume": file.filename, "score": match_score})

    return {"message": "Resume uploaded", "match_score": match_score}

@app.get("/api/shortlist/{job_id}")
async def get_shortlisted(job_id: int):
    candidates = [r for r in shortlisted if r["job_id"] == job_id]
    return candidates

@app.post("/api/schedule-interview")
async def schedule_interview(
    name: str = Form(...),
    email: str = Form(...),
    job_title: str = Form(...),
    interview_time: str = Form(...),
    interview_location: str = Form(...)
):
    email_body = f"""
Hi {name},

Your interview for the position of {job_title} is scheduled at {interview_time}.
Location: {interview_location}

Good luck!
"""

    return {
        "message": "Interview scheduled",
        "data": {
            "name": name,
            "email": email,
            "job_title": job_title,
            "interview_time": interview_time,
            "interview_location": interview_location
        },
        "email_body": email_body.strip()
    }
