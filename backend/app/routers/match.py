from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db import models, crud
from app.agents.match_scoring import calculate_match_score
from app.agents.resume_extractor import extract_resume_data

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/match-resume")
def match_resume(resume_text: str = Form(...), job_id: int = Form(...), db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        return {"error": "Job not found"}

    jd_data = {
        "Job Title": job.title,
        "Required Skills": job.skills,
        "Years of Experience": job.experience,
        "Educational Qualifications": job.education,
        "Job Responsibilities": job.responsibilities,
    }

    resume_data = extract_resume_data(resume_text)
    score_data = calculate_match_score(jd_data, resume_data)
    candidate = crud.create_candidate(db, resume_data, score_data, job_id)

    return {
        "match_score": score_data.get("score"),
        "explanation": score_data.get("explanation"),
        "shortlisted": candidate.shortlisted
    }
