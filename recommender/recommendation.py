# recommender/recommendation.py

from recommender.similarity import (
    calculate_skill_match,
    calculate_text_match,
    calculate_final_score
)

from recommender.skill_gap import analyze_skill_gap

from recommender.skill_priority import (
    calculate_skill_priority
)

from recommender.learning_recommendation import (
    generate_learning_recommendations
)

from recommender.career_roadmap import (
    generate_career_roadmap
)


def recommend_jobs(profile, jobs):

    results = []

    for _, job in jobs.iterrows():

        # ==================================================
        # 1. REQUIRED SKILLS
        # ==================================================

        required_skills = [
            skill.strip().lower()
            for skill in job["required_skills"].split(",")
            if skill.strip()
        ]

        # Candidate skills
        candidate_skills = [
            skill.strip().lower()
            for skill in profile.get("skills", [])
            if skill.strip()
        ]

        # ==================================================
        # 2. SKILL MATCH
        # ==================================================

        skill_score = calculate_skill_match(
            candidate_skills,
            required_skills
        )

        # ==================================================
        # 3. EDUCATION MATCH
        # ==================================================

        education_text = " ".join(
            profile.get("education", [])
        ).lower()

        education_score = calculate_text_match(
            education_text,
            str(job["education"])
        )

        # ==================================================
        # 4. PROJECT MATCH
        # ==================================================

        project_text = " ".join(
            profile.get("projects", [])
        ).lower()

        project_score = calculate_text_match(
            project_text,
            str(job["description"])
        )

        # ==================================================
        # 5. EXPERIENCE MATCH
        # ==================================================

        experience_text = " ".join(
            profile.get("experience", [])
        ).lower()

        experience_score = calculate_text_match(
            experience_text,
            str(job["description"])
        )

        # ==================================================
        # 6. FINAL JOB SCORE
        # ==================================================

        final_score = calculate_final_score(
            skill_score,
            education_score,
            project_score,
            experience_score
        )

        # ==================================================
        # 7. SKILL GAP ANALYSIS
        # ==================================================

        skill_gap = analyze_skill_gap(
            candidate_skills,
            required_skills
        )

        matching_skills = skill_gap["matching_skills"]

        missing_skills = skill_gap["missing_skills"]

        skill_coverage = skill_gap["coverage"]

        # ==================================================
        # 8. SKILL PRIORITY
        # ==================================================

        skill_priorities = calculate_skill_priority(
            missing_skills,
            required_skills,
            job["job_title"]
        )

        # ==================================================
        # 9. LEARNING RECOMMENDATIONS
        # ==================================================

        learning_recommendations = (
            generate_learning_recommendations(
                skill_priorities
            )
        )

        # ==================================================
        # 10. CAREER ROADMAP
        # ==================================================

        career_roadmap = generate_career_roadmap(
            job["job_title"],
            candidate_skills,
            missing_skills,
            skill_priorities
        )

        # ==================================================
        # 11. STORE COMPLETE RESULT
        # ==================================================

        results.append({

            "job_id": job["job_id"],

            "job_title": job["job_title"],

            "company": job["company"],

            "score": final_score,

            "skill_score": round(
                skill_score,
                2
            ),

            "education_score": round(
                education_score,
                2
            ),

            "project_score": round(
                project_score,
                2
            ),

            "experience_score": round(
                experience_score,
                2
            ),

            "description": job["description"],

            # Skill gap
            "matching_skills":
                matching_skills,

            "missing_skills":
                missing_skills,

            "skill_coverage":
                skill_coverage,

            # Priority
            "skill_priorities":
                skill_priorities,

            # Learning
            "learning_recommendations":
                learning_recommendations,

            # Career roadmap
            "career_roadmap":
                career_roadmap
        })

    # ======================================================
    # 12. SORT BY BEST MATCH
    # ======================================================

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results
