from parser.resume_parser import extract_resume_text
from parser.info_extractor import extract_projects


file_path = "uploads/dresume.pdf"

text = extract_resume_text(file_path)

projects = extract_projects(text)

print("Projects Found:")

for project in projects:
    print("-", project)