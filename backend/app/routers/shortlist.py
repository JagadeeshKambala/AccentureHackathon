from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/shortlist/{job_id}")
def get_shortlisted_candidates(job_id: int, db: Session = Depends(get_db)):
    candidates = db.query(models.Candidate).filter(
        models.Candidate.job_id == job_id,
        models.Candidate.shortlisted == True
    ).all()

    return [
        {
            "name": c.name,
            "email": c.email,
            "match_score": c.match_score,
            "explanation": c.explanation
        } for c in candidates
    ]
