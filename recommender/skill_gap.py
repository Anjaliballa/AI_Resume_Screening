def analyze_skill_gap(candidate_skills, required_skills):
    """
    Analyze the candidate's skill gap for a job.

    Returns:
        matching_skills: skills candidate already has
        missing_skills: skills candidate needs
        coverage: percentage of required skills covered
    """

    candidate_set = {
        skill.strip().lower()
        for skill in candidate_skills
    }

    required_set = {
        skill.strip().lower()
        for skill in required_skills
    }

    matching_skills = sorted(
        candidate_set.intersection(required_set)
    )

    missing_skills = sorted(
        required_set.difference(candidate_set)
    )

    if not required_set:
        coverage = 0
    else:
        coverage = (
            len(matching_skills) /
            len(required_set)
        ) * 100

    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "coverage": round(coverage, 2)
    }
