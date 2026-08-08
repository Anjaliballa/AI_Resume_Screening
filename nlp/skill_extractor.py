import re

from nlp.skills_list import SKILLS


def extract_skills(text):
    """
    Extract technical skills from resume text.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        # Escape special characters in the skill
        escaped_skill = re.escape(skill)

        # Create word-boundary pattern
        pattern = r"\b" + escaped_skill + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills