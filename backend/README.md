AI Agent Execution Process – Job Screening AI System
This system uses a multi-agent architecture to streamline recruitment tasks using on-prem LLMs (via Ollama) and custom Python agents. Below is the detailed process of how each agent functions in coordination with the backend and frontend.
📌 1. Upload Job Description (JD Agent)
Frontend: A form allows uploading a .txt, .pdf, or .docx file containing the job description.
Backend Route: /api/upload-jd
Agent Process:
Extracts the text from the uploaded file.
Sends it to a local LLM (e.g., Mistral or Gemma via Ollama) for summarization.
Stores the summarized JD in the database (SQLite) with a unique job ID.
Output: Returns a summary and Job ID to the frontend.
📌 2. Upload Resume (Resume Parser & Matcher Agent)
Frontend: A form where the user uploads a resume and selects the corresponding Job ID.
Backend Route: /api/upload-resume
Agent Process:
Extracts content from resume (.pdf/.docx).
Retrieves the JD summary for the selected Job ID.
Sends both to the matching agent (powered by the LLM) to compute:
Candidate profile summary
Relevance/match score
Stores the parsed candidate profile and score in the database.
Output: Displays the candidate's match score for the job role.
📌 3. Shortlisting Agent
Backend Route: /api/shortlist-candidates
Agent Process:
Compares all stored candidate scores for a selected Job ID.
Filters and returns candidates who exceed a threshold (e.g., 70% match score).
Output: Returns a list of shortlisted candidates with names and scores.
📌 4. Interview Scheduler Agent
Frontend: A form where the recruiter inputs:
Candidate name
Job ID
Interview date and time
Backend Route: /api/schedule-interview
Agent Process:
Verifies candidate and job entry.
Generates a formatted email or calendar invite message.
Schedules the interview (message is returned for email integration).
Output: Displays a success message with interview details ready for sending.
🧠 LLM Integration
All agents interact with local LLMs using Ollama and models like:
mistral
gemma:2b
Communication occurs via API-like functions that process job/resume context and return structured responses.
