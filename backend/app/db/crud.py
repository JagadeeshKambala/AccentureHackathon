from sqlalchemy.orm import Session
from app.db import models

def create_job(db: Session, jd_data: dict):
    job = models.Job(
        title=jd_data.get("Job Title"),
        summary=jd_data.get("Job Responsibilities"),
        skills=", ".join(jd_data.get("Required Skills", [])) if isinstance(jd_data.get("Required Skills"), list) else jd_data.get("Required Skills"),
        experience=jd_data.get("Years of Experience"),
        education=jd_data.get("Education"),
        responsibilities=jd_data.get("Responsibilities"),
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def create_candidate(db: Session, resume_data: dict, match_score: dict, job_id: int):
    candidate = models.Candidate(
        name=resume_data.get("Candidate Name"),
        email=resume_data.get("Email"),
        phone=resume_data.get("Phone"),
        skills=", ".join(resume_data.get("Skills", [])) if isinstance(resume_data.get("Skills"), list) else resume_data.get("Skills"),
        experience=resume_data.get("Work Experience"),
        education=resume_data.get("Education"),
        certifications=resume_data.get("Certifications"),
        match_score=match_score.get("score"),
        explanation=match_score.get("explanation"),
        shortlisted=match_score.get("score", 0) >= 80,
        job_id=job_id
    )
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate
