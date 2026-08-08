from recommender.similarity import (
    calculate_skill_match,
    calculate_text_match,
    calculate_final_score
)


def recommend_jobs(profile, jobs):

    results = []

    for _, job in jobs.iterrows():

        # Required skills from job
        required_skills = [
            skill.strip().lower()
            for skill in job["required_skills"].split(",")
        ]


        # Skill score
        skill_score = calculate_skill_match(
            profile["skills"],
            required_skills
        )


        # Education score
        education_text = " ".join(
            profile["education"]
        ).lower()

        education_score = calculate_text_match(
            education_text,
            job["education"]
        )


        # Project score
        project_text = " ".join(
            profile["projects"]
        )

        project_score = calculate_text_match(
            project_text,
            job["description"]
        )


        # Experience score
        experience_text = " ".join(
            profile["experience"]
        )

        experience_score = calculate_text_match(
            experience_text,
            job["description"]
        )


        # Final weighted score
        final_score = calculate_final_score(
            skill_score,
            education_score,
            project_score,
            experience_score
        )


        results.append({

            "job_title": job["job_title"],

            "company": job["company"],

            "score": final_score,

            "description": job["description"]

        })


    # Highest score first

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return results