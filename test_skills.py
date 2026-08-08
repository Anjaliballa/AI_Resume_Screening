from parser.resume_parser import extract_resume_text
from nlp.skill_extractor import extract_skills


file_path = "uploads/dresume.pdf"

text = extract_resume_text(file_path)

skills = extract_skills(text)

print("Skills Found:")

for skill in skills:
    print("-", skill)