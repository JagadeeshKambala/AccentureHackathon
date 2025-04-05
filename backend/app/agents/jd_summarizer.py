import json
import re
from app.core.ollama_runner import query_ollama

def summarize_job_description(jd_text: str) -> dict:
    """
    Query the Ollama model and extract a clean JSON summary from the response.
    Handles comment stripping and trailing commas.
    """

    prompt = f"""
Extract the following job description into JSON format with the following keys:
- Job Title
- Required Skills
- Years of Experience
- Education
- Responsibilities

Only return a valid JSON object. Do not include explanations or comments.

Job Description:
\"\"\"
{jd_text}
\"\"\"
"""

    response = query_ollama("mistral", prompt)
    print("🔍 LLM raw response:\n", response)

    try:
        # Extract JSON-like block from the model response
        match = re.search(r"\{[\s\S]*?\}", response)
        if not match:
            raise ValueError("No JSON object found in response.")

        json_block = match.group(0)

        # Strip JS-style comments
        json_block = re.sub(r"//.*", "", json_block)

        # Remove trailing commas (before closing braces or brackets)
        json_block = re.sub(r",\s*([}\]])", r"\1", json_block)

        # Parse with standard json
        parsed = json.loads(json_block)
        return parsed

    except Exception as e:
        print("❌ Final JSON parsing failed:", e)
        return {"raw_response": response}
