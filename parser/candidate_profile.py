from parser.resume_parser import extract_resume_text
from parser.info_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_education,
    extract_experience,
    extract_projects
)
from nlp.skill_extractor import extract_skills


def create_candidate_profile(file_path):
    """
    Extract all important information from a resume
    and create a structured candidate profile.
    """

    # Extract raw text from resume
    text = extract_resume_text(file_path)

    # Extract candidate information
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)

    # Extract skills
    skills = extract_skills(text)

    # Extract education
    education = extract_education(text)

    # Extract experience
    experience = extract_experience(text)

    # Extract projects
    projects = extract_projects(text)

    # Create candidate profile
    profile = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects
    }

    return profile