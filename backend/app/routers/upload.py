from fastapi import APIRouter, UploadFile, Form, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.agents.jd_summarizer import summarize_job_description
from app.agents.resume_extractor import extract_resume_data
from app.db import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload-jd")
async def upload_jd(text: str = Form(...), db: Session = Depends(get_db)):
    jd_data = summarize_job_description(text)
    job = crud.create_job(db, jd_data)
    return {"job_id": job.id, "summary": jd_data}

@router.post("/upload-resume")
async def upload_resume(text: str = Form(...), job_id: int = Form(...), db: Session = Depends(get_db)):
    resume_data = extract_resume_data(text)
    return {"resume_data": resume_data}
