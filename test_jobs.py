from recommender.job_loader import load_jobs
file_path = "datasets/jobs.csv"
jobs = load_jobs(file_path)
print("===== JOB DATASET =====")
print(jobs)
print("\nNumber of jobs:", len(jobs))
