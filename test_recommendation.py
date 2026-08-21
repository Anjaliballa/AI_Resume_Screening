from recommender.job_loader import load_jobs
from recommender.recommendation import recommend_jobs
# Example for a candidate profile
profile = {
    "skills": [
        "python",
        "c",
        "html",
        "css",
        "react",
        "sql",
        "dbms",
        "machine learning",
        "numpy",
        "pandas",
        "git",
        "github",
        "jupyter",
        "computer vision"
    ],

    "education": [
        "B.Tech in Computer Science"
    ],

    "projects": [
        "Machine Learning Telecom Customer Churn Prediction",
        "Rubik Cube Solver using AI",
        "Computer Vision"
    ],

    "experience": []
}
# to load jobs
jobs = load_jobs("datasets/jobs.csv")

#to generate recommendations
recommendations = recommend_jobs(
    profile,
    jobs
)
print("\n===== EXPLAINABLE JOB RECOMMENDATIONS =====\n")
for i, job in enumerate(recommendations, 1):

    print(f"{i}. {job['job_title']}")
    print(f"   Company: {job['company']}")
    print(f"   Overall Match: {job['score']}%")

    print(f"   Skills Match: {job['skill_score']}%")
    print(f"   Education Match: {job['education_score']}%")
    print(f"   Project Match: {job['project_score']}%")
    print(f"   Experience Match: {job['experience_score']}%")

    print(
        f"   Matching Skills: "
        f"{', '.join(job['matching_skills'])}"
    )

    print(
        f"   Missing Skills: "
        f"{', '.join(job['missing_skills'])}"
    )
    print(
    f"   Skill Coverage: "
    f"{job['skill_coverage']}%"
    )
    print(
    f"   Skill Priorities: "
    f"{job['skill_priorities']}"
    )
    print()
