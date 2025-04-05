from sqlalchemy.orm import Session
from app.db import models
from app.core.config import DEFAULT_MATCH_THRESHOLD

def shortlist_candidates(db: Session, job_id: int, threshold: int = DEFAULT_MATCH_THRESHOLD):
    """
    Marks candidates as shortlisted if their score exceeds the threshold.
    Returns list of shortlisted candidates.
    """
    candidates = db.query(models.Candidate).filter(models.Candidate.job_id == job_id).all()

    shortlisted = []
    for candidate in candidates:
        if candidate.match_score >= threshold:
            candidate.shortlisted = True
            shortlisted.append(candidate)

    db.commit()
    return shortlisted
