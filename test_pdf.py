from parser.pdf_parser import extract_text_from_pdf

pdf_path = "uploads/dresume.pdf"   # Change this to your actual PDF filename

text = extract_text_from_pdf(pdf_path)

print(text)