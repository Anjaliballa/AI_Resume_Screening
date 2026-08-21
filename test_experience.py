from parser.resume_parser import extract_resume_text
from parser.info_extractor import extract_experience
file_path = "uploads/dresume.pdf"
text = extract_resume_text(file_path)
experience = extract_experience(text)
print("Experience Found:")
for item in experience:
    print("-", item)
