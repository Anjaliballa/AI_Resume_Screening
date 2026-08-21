from parser.resume_parser import extract_resume_text
from parser.info_extractor import extract_email, extract_phone, extract_name
file_path = "uploads/dresume.pdf"
text = extract_resume_text(file_path)
email = extract_email(text)
phone = extract_phone(text)
name = extract_name(text)
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
