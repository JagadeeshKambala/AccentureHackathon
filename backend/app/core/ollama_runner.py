import subprocess

def query_ollama(model: str, prompt: str) -> str:
    """
    Properly query an Ollama model and return the complete response string.
    """
    try:
        print(f"🔄 Running Ollama model: {model}...")

        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        stdout = result.stdout.decode("utf-8").strip()
        stderr = result.stderr.decode("utf-8").strip()

        if stderr:
            print("⚠️ Ollama STDERR:", stderr)

        print("✅ Ollama STDOUT:", stdout)
        return stdout

    except subprocess.TimeoutExpired:
        print("❌ Ollama call timed out.")
        return ""
    except Exception as e:
        print(f"❌ Ollama query failed: {e}")
        return ""
