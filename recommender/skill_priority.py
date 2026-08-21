def calculate_skill_priority(
    missing_skills,
    required_skills,
    job_title
):
    """
    Calculate role-aware priority for missing skills.

    Priority is based on how important a skill is
    for the target job role.
    """

    role_core_skills = {

        "machine learning intern": [
            "machine learning",
            "scikit-learn",
            "pandas",
            "numpy"
        ],

        "data science intern": [
            "python",
            "pandas",
            "numpy",
            "sql",
            "machine learning"
        ],

        "python developer intern": [
            "python",
            "flask",
            "sql",
            "git",
            "github"
        ],

        "ai intern": [
            "artificial intelligence",
            "machine learning",
            "computer vision",
            "python"
        ],

        "web developer intern": [
            "html",
            "css",
            "javascript",
            "react",
            "flask"
        ],

        "data analyst intern": [
            "python",
            "sql",
            "pandas",
            "excel"
        ],

        "nlp intern": [
            "nlp",
            "nltk",
            "spacy",
            "machine learning",
            "python"
        ],

        "computer vision intern": [
            "computer vision",
            "opencv",
            "machine learning",
            "python"
        ],

        "software engineer intern": [
            "python",
            "java",
            "sql",
            "git",
            "data structures"
        ],

        "ml engineer intern": [
            "machine learning",
            "deep learning",
            "pytorch",
            "tensorflow",
            "python"
        ]
    }

    job_title = job_title.lower().strip()

    core_skills = role_core_skills.get(
        job_title,
        required_skills
    )

    priorities = {}

    for skill in missing_skills:

        skill = skill.lower().strip()

        if skill not in core_skills:
            priorities[skill] = {
                "priority": "LOW",
                "score": 20
            }
            continue

        position = core_skills.index(skill)

        total = len(core_skills)

        # Earlier skills are more important
        score = (
            (total - position) / total
        ) * 100

        if score >= 75:
            priority = "HIGH"

        elif score >= 40:
            priority = "MEDIUM"

        else:
            priority = "LOW"

        priorities[skill] = {
            "priority": priority,
            "score": round(score, 2)
        }

    return priorities
