from recommender.similarity import calculate_skill_match


candidate_skills = [
    "python",
    "sql",
    "pandas",
    "machine learning"
]

required_skills = [
    "python",
    "pandas",
    "machine learning",
    "tensorflow"
]


score = calculate_skill_match(
    candidate_skills,
    required_skills
)


print("Skill Match Score:", score)