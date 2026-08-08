import os

from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx


def extract_resume_text(file_path):
    """
    Extract text from a resume file (PDF or DOCX).

    Parameters:
        file_path (str): Path to the uploaded resume.

    Returns:
        str: Extracted resume text.
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")