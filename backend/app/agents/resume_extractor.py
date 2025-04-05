from app.core.ollama_runner import query_ollama
import json, re

def extract_resume_data(resume_text: str) -> dict:
    prompt = f"""
Extract the following fields from the resume:

- Candidate Name
- Email
- Phone
- Skills (comma-separated string)
- Work Experience (short summary)
- Education (short summary)
- Certifications

⚠️ ONLY return a single valid JSON object. No lists, no code blocks, no explanations, no markdown. Do not include <|...|> placeholders.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    response = query_ollama("mistral", prompt)
    print("🔍 Resume Extractor raw response:\n", response)

    try:
        # Remove any markdown and multiline blocks
        cleaned = re.sub(r"```.*?```", "", response, flags=re.DOTALL)
        cleaned = re.sub(r"JSON:\n", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"//.*", "", cleaned)
        cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)

        # Extract only the first valid JSON object
        match = re.search(r"\{[\s\S]*?\}", cleaned)
        if match:
            return json.loads(match.group(0))

        raise ValueError("No valid JSON object found.")

    except Exception as e:
        print("❌ Resume JSON parsing failed:", e)
        return {"raw_response": response}
