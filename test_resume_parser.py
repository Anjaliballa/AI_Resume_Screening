from parser.resume_parser import extract_resume_text

file_path = "uploads/resume_final.docx"

text = extract_resume_text(file_path)

print(text)