from docx import Document


def extract_text_from_docx(docx_path):

    text = ""

    document = Document(docx_path)

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text