from app.core.ollama_runner import query_ollama

def generate_interview_email(candidate_name: str, job_title: str) -> str:
    """
    Use LLM to generate a friendly, professional interview email.
    """
    prompt = f"""
You are an AI HR assistant.

Compose a professional and friendly interview invitation email for the candidate "{candidate_name}" applying for the role of "{job_title}".

Include:
- A warm greeting
- 3 proposed time slots (next week)
- Mention it's a virtual interview
- Contact email (e.g., hr@example.com)
- A closing thank-you

Format it as plain text (no markdown or HTML).
"""

    return query_ollama("mistral", prompt)
