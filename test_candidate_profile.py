from parser.candidate_profile import create_candidate_profile


file_path = "uploads/dresume.pdf"

profile = create_candidate_profile(file_path)

print("\n===== CANDIDATE PROFILE =====")

print("\nName:")
print(profile["name"])

print("\nEmail:")
print(profile["email"])

print("\nPhone:")
print(profile["phone"])

print("\nSkills:")
for skill in profile["skills"]:
    print("-", skill)

print("\nEducation:")
for education in profile["education"]:
    print("-", education)

print("\nExperience:")
for experience in profile["experience"]:
    print("-", experience)

print("\nProjects:")
for project in profile["projects"]:
    print("-", project)
    