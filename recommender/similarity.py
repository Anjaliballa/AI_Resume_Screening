import re


def calculate_skill_match(candidate_skills, required_skills):
    """
    Calculate skill matching percentage.
    """

    candidate_skills = set(
        skill.lower()
        for skill in candidate_skills
    )

    required_skills = set(
        skill.lower()
        for skill in required_skills
    )

    if not required_skills:
        return 0

    matched = candidate_skills.intersection(
        required_skills
    )

    return (len(matched) / len(required_skills)) * 100



def calculate_text_match(candidate_text, job_text):
    """
    Calculate simple text similarity.
    """

    candidate_text = candidate_text.lower()
    job_text = job_text.lower()

    words = re.findall(
        r'\b[a-zA-Z]+\b',
        candidate_text
    )

    job_words = set(
        re.findall(
            r'\b[a-zA-Z]+\b',
            job_text
        )
    )

    if not words:
        return 0

    matched = 0

    for word in words:
        if word in job_words:
            matched += 1

    return (matched / len(words)) * 100



def calculate_final_score(
        skills_score,
        education_score,
        project_score,
        experience_score
):
    """
    Weighted final recommendation score.
    """

    final_score = (
        skills_score * 0.60 +
        education_score * 0.20 +
        project_score * 0.15 +
        experience_score * 0.05
    )

    return round(final_score, 2)