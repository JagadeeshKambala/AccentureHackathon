from app.core.ollama_runner import query_ollama

def calculate_match_score(jd_data: dict, resume_data: dict) -> dict:
    prompt = f"""
Compare the following job description and candidate profile.

Job Description:
Title: {jd_data.get("Job Title", "")}
Skills: {jd_data.get("Required Skills", "")}
Experience: {jd_data.get("Years of Experience", "")}
Education: {jd_data.get("Educational Qualifications", "")}
Responsibilities: {jd_data.get("Job Responsibilities", "")}

Candidate Profile:
Name: {resume_data.get("Candidate Name", "")}
Skills: {resume_data.get("Skills", "")}
Experience: {resume_data.get("Work Experience", "")}
Education: {resume_data.get("Education", "")}
Certifications: {resume_data.get("Certifications", "")}

Provide:
1. Match Score out of 100 based on relevance.
2. A short explanation of the match.

Return result in JSON format like:
{{"score": 87, "explanation": "Good skill alignment..."}}
"""

    response = query_ollama("mistral", prompt)

    try:
        import json
        return json.loads(response)
    except Exception as e:
        print("Failed to parse match score:", e)
        return {"raw_response": response}
