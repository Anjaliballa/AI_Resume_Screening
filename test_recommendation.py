from parser.candidate_profile import create_candidate_profile
from recommender.job_loader import load_jobs
from recommender.recommendation import recommend_jobs


# Resume
resume_path = "uploads/dresume.pdf"

# Create candidate profile
profile = create_candidate_profile(resume_path)

# Load jobs
jobs = load_jobs("datasets/jobs.csv")

# Generate recommendations
recommendations = recommend_jobs(
    profile,
    jobs
)

print("\n===== JOB RECOMMENDATIONS =====")

for job in recommendations:

    print(
        f"{job['job_title']} | "
        f"{job['company']} | "
        f"Match: {job['score']}%"
    )