from parser.resume_parser import extract_resume_text
from parser.info_extractor import extract_education
file_path = "uploads/dresume.pdf"
text = extract_resume_text(file_path)
education = extract_education(text)
print("Education Found:")
for item in education:
    print("-", item)
