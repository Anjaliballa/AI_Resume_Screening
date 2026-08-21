# recommender/resume_improvement.py

def analyze_resume_improvement(profile):
    """
    Analyze a candidate profile and generate resume improvement suggestions.
    """

    suggestions = []
    strengths = []
    warnings = []

    # --------------------------------------------------
    # Get profile information safely
    # --------------------------------------------------

    name = profile.get("name", "")
    email = profile.get("email", "")
    phone = profile.get("phone", "")

    skills = profile.get("skills", [])
    education = profile.get("education", [])
    projects = profile.get("projects", [])
    experience = profile.get("experience", [])

    # Convert to lists if necessary
    if not isinstance(skills, list):
        skills = [skills] if skills else []

    if not isinstance(education, list):
        education = [education] if education else []

    if not isinstance(projects, list):
        projects = [projects] if projects else []

    if not isinstance(experience, list):
        experience = [experience] if experience else []

    # --------------------------------------------------
    # 1. CONTACT INFORMATION
    # --------------------------------------------------

    if name:
        strengths.append("Candidate name detected.")
    else:
        suggestions.append({
            "category": "Contact Information",
            "priority": "HIGH",
            "issue": "Candidate name is missing.",
            "suggestion": "Add your full name at the top of the resume."
        })

    if email:
        strengths.append("Email address detected.")
    else:
        suggestions.append({
            "category": "Contact Information",
            "priority": "HIGH",
            "issue": "Email address is missing.",
            "suggestion": "Add a professional email address."
        })

    if phone:
        strengths.append("Phone number detected.")
    else:
        suggestions.append({
            "category": "Contact Information",
            "priority": "MEDIUM",
            "issue": "Phone number is missing.",
            "suggestion": "Add your phone number so recruiters can contact you."
        })

    # --------------------------------------------------
    # 2. SKILLS
    # --------------------------------------------------

    if len(skills) == 0:

        suggestions.append({
            "category": "Technical Skills",
            "priority": "HIGH",
            "issue": "No technical skills detected.",
            "suggestion": "Add relevant programming languages, tools, frameworks and technologies."
        })

    elif len(skills) < 5:

        suggestions.append({
            "category": "Technical Skills",
            "priority": "HIGH",
            "issue": "Very few technical skills detected.",
            "suggestion": "Add more relevant technical skills that you genuinely know."
        })

    else:

        strengths.append(
            f"{len(skills)} technical skills detected."
        )

    # --------------------------------------------------
    # 3. EDUCATION
    # --------------------------------------------------

    if len(education) == 0:

        suggestions.append({
            "category": "Education",
            "priority": "HIGH",
            "issue": "Education information was not detected.",
            "suggestion": "Add your degree, university/college and relevant academic details."
        })

    else:

        strengths.append("Education information detected.")

    # --------------------------------------------------
    # 4. PROJECTS
    # --------------------------------------------------

    if len(projects) == 0:

        suggestions.append({
            "category": "Projects",
            "priority": "HIGH",
            "issue": "No projects were detected.",
            "suggestion": "Add 2-3 relevant technical projects with technologies and measurable results."
        })

    elif len(projects) == 1:

        suggestions.append({
            "category": "Projects",
            "priority": "MEDIUM",
            "issue": "Only one project was detected.",
            "suggestion": "Consider adding another relevant project demonstrating different technical skills."
        })

    else:

        strengths.append(
            f"{len(projects)} projects detected."
        )

    # --------------------------------------------------
    # 5. EXPERIENCE
    # --------------------------------------------------

    if len(experience) == 0:

        suggestions.append({
            "category": "Experience",
            "priority": "MEDIUM",
            "issue": "No professional experience was detected.",
            "suggestion": "If you have internships, freelance work, volunteering or relevant practical experience, include them."
        })

    else:

        strengths.append(
            f"{len(experience)} experience entries detected."
        )

    # --------------------------------------------------
    # 6. PROJECT QUALITY
    # --------------------------------------------------

    project_text = " ".join(
        str(project) for project in projects
    ).lower()

    achievement_keywords = [
        "accuracy",
        "performance",
        "improved",
        "increased",
        "reduced",
        "%",
        "users",
        "dataset",
        "model",
        "prediction",
        "deployed"
    ]

    achievement_found = any(
        keyword in project_text
        for keyword in achievement_keywords
    )

    if projects and not achievement_found:

        suggestions.append({
            "category": "Project Impact",
            "priority": "MEDIUM",
            "issue": "Project descriptions may lack measurable results.",
            "suggestion": "Add metrics such as accuracy, performance improvement, dataset size or number of users."
        })

    # --------------------------------------------------
    # 7. AI / ML PROJECT SIGNAL
    # --------------------------------------------------

    ai_ml_keywords = [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "computer vision",
        "nlp",
        "tensorflow",
        "pytorch",
        "scikit-learn"
    ]

    ai_ml_found = [
        skill for skill in skills
        if any(
            keyword in str(skill).lower()
            for keyword in ai_ml_keywords
        )
    ]

    if ai_ml_found:

        strengths.append(
            "AI/ML skills detected: "
            + ", ".join(ai_ml_found)
        )

    # --------------------------------------------------
    # 8. GITHUB / PORTFOLIO
    # --------------------------------------------------

    full_text = (
        " ".join(map(str, skills))
        + " "
        + " ".join(map(str, projects))
        + " "
        + " ".join(map(str, experience))
    ).lower()

    github_found = (
        "github" in full_text
        or "git hub" in full_text
    )

    if github_found:

        strengths.append(
            "GitHub/portfolio reference detected."
        )

    else:

        suggestions.append({
            "category": "Portfolio",
            "priority": "MEDIUM",
            "issue": "No GitHub or portfolio reference detected.",
            "suggestion": "Add your GitHub profile or portfolio if available."
        })

    # --------------------------------------------------
    # 9. GENERAL RESUME QUALITY
    # --------------------------------------------------

    total_sections = 5

    completed_sections = 0

    if name or email or phone:
        completed_sections += 1

    if skills:
        completed_sections += 1

    if education:
        completed_sections += 1

    if projects:
        completed_sections += 1

    if experience:
        completed_sections += 1

    resume_completeness = round(
        (completed_sections / total_sections) * 100,
        2
    )

    # --------------------------------------------------
    # 10. RESUME SCORE
    # --------------------------------------------------

    score = 100

    for suggestion in suggestions:

        if suggestion["priority"] == "HIGH":
            score -= 15

        elif suggestion["priority"] == "MEDIUM":
            score -= 8

        else:
            score -= 3

    score = max(0, min(100, score))

    # --------------------------------------------------
    # 11. FINAL RESULT
    # --------------------------------------------------

    return {
        "resume_score": score,
        "resume_completeness": resume_completeness,
        "strengths": strengths,
        "warnings": warnings,
        "suggestions": suggestions
    }
