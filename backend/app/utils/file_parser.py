import os
from pdfminer.high_level import extract_text as extract_pdf_text  # type: ignore
from docx import Document  # type: ignore
def extract_text_from_file(file_path: str) -> str:
    _, ext = os.path.splitext(file_path)

    if ext.lower() == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext.lower() == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are supported.")

def extract_text_from_pdf(file_path: str) -> str:
    try:
        return extract_pdf_text(file_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""
