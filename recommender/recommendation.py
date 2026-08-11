from recommender.similarity import (
    calculate_skill_match,
    calculate_text_match,
    calculate_final_score
)


def recommend_jobs(profile, jobs):

    results = []

    # Candidate skills
    candidate_skills = [
        skill.strip().lower()
        for skill in profile.get("skills", [])
    ]

    for _, job in jobs.iterrows():

        # -----------------------------------
        # 1. Required skills
        # -----------------------------------

        required_skills = [
            skill.strip().lower()
            for skill in job["required_skills"].split(",")
        ]

        # -----------------------------------
        # 2. Matching and missing skills
        # -----------------------------------

        candidate_skill_set = set(candidate_skills)
        required_skill_set = set(required_skills)

        matching_skills = sorted(
            candidate_skill_set.intersection(
                required_skill_set
            )
        )

        missing_skills = sorted(
            required_skill_set.difference(
                candidate_skill_set
            )
        )

        # -----------------------------------
        # 3. Skill score
        # -----------------------------------

        skill_score = calculate_skill_match(
            candidate_skills,
            required_skills
        )

        # -----------------------------------
        # 4. Education score
        # -----------------------------------

        education_text = " ".join(
            profile.get("education", [])
        ).lower()

        education_score = calculate_text_match(
            education_text,
            job["education"]
        )

        # -----------------------------------
        # 5. Project score
        # -----------------------------------

        project_text = " ".join(
            profile.get("projects", [])
        ).lower()

        project_score = calculate_text_match(
            project_text,
            job["description"]
        )

        # -----------------------------------
        # 6. Experience score
        # -----------------------------------

        experience_text = " ".join(
            profile.get("experience", [])
        ).lower()

        experience_score = calculate_text_match(
            experience_text,
            job["description"]
        )

        # -----------------------------------
        # 7. Final weighted score
        # -----------------------------------

        final_score = calculate_final_score(
            skill_score,
            education_score,
            project_score,
            experience_score
        )

        # -----------------------------------
        # 8. Store complete result
        # -----------------------------------

        results.append({

            "job_title": job["job_title"],

            "company": job["company"],

            "score": final_score,

            "skill_score": round(skill_score, 2),

            "education_score": round(
                education_score, 2
            ),

            "project_score": round(
                project_score, 2
            ),

            "experience_score": round(
                experience_score, 2
            ),

            "matching_skills": matching_skills,

            "missing_skills": missing_skills,

            "description": job["description"]

        })

    # -----------------------------------
    # Sort highest score first
    # -----------------------------------

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results
