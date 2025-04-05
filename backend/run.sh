#!/bin/bash

echo "🚀 Starting Ollama-backed AI Recruitment Backend..."

# Activate virtual environment
source .venv/bin/activate

# Optional: Check if Ollama is running (or remind user)
if ! pgrep -f "ollama serve" > /dev/null; then
  echo "⚠️ Ollama is not running. Please open a separate terminal and run: ollama serve"
else
  echo "✅ Ollama is running."
fi

# Launch FastAPI app with live reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
