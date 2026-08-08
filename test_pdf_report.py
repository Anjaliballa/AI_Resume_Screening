from parser.candidate_profile import create_candidate_profile
from recommender.job_loader import load_jobs
from recommender.recommendation import recommend_jobs
from reports.pdf_report_generator import generate_pdf_report


resume = "uploads/dresume.pdf"


profile = create_candidate_profile(
    resume
)


jobs = load_jobs(
    "datasets/jobs.csv"
)


recommendations = recommend_jobs(
    profile,
    jobs
)


pdf = generate_pdf_report(
    profile,
    recommendations
)


print("PDF Created:")
print(pdf)
