from parser.docx_parser import extract_text_from_docx


docx_path = "uploads/resume_final.docx"

text = extract_text_from_docx(docx_path)

print(text)