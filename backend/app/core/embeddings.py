import subprocess
import json

def get_embedding(text: str, model: str = "tinyllama") -> list:
    """
    Simulate generating an embedding vector using a local Ollama LLM.
    Prompts the model to return a 50-dimensional vector of floats.
    """
    prompt = f"""
You are an AI that transforms text into numerical vector embeddings.

Given the following input, generate a 50-dimensional embedding. Return ONLY the embedding list in JSON format (e.g., [0.1, 0.23, ...]).

Input:
\"\"\"
{text}
\"\"\"
"""

    try:
        process = subprocess.Popen(
            ["ollama", "run", model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=prompt.encode())

        if stderr:
            raise RuntimeError(stderr.decode())

        response = stdout.decode().strip()

        # Try to parse it as JSON list
        embedding = json.loads(response)
        if isinstance(embedding, list) and all(isinstance(x, (float, int)) for x in embedding):
            return embedding
        else:
            raise ValueError("Invalid embedding format")

    except Exception as e:
        print(f"Error generating mock embedding: {e}")
        return []
