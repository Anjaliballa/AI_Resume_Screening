from parser.resume_parser import extract_resume_text
from nlp.preprocess import preprocess_text
file_path = "uploads/dresume.pdf"
text = extract_resume_text(file_path)
tokens = preprocess_text(text)
print(tokens)
