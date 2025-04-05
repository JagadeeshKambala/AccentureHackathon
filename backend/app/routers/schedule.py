from fastapi import APIRouter, Form
from app.core.ollama_runner import query_ollama

router = APIRouter()

@router.post("/schedule-interview")
def schedule_interview(candidate_name: str = Form(...), email: str = Form(...), job_title: str = Form(...)):
    prompt = f"""
Write a professional interview invitation email for a candidate named {candidate_name} who applied for the job "{job_title}".
Suggest 3 time slots for the next week, mention the interview will be virtual, and include a friendly tone.

Reply in plain email format.
"""

    response = query_ollama("mistral", prompt)
    return {
        "email_to": email,
        "email_body": response
    }
