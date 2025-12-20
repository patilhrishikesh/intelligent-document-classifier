import pdfplumber
from docx import Document

def extract_text_from_txt(file) -> str:
    return file.read().decode("utf-8")

def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_doc(file) -> str:
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file, file_type: str) -> str:
    if file_type == "txt":
        return extract_text_from_txt(file)
    
    elif file_type == "pdf":
        return extract_text_from_pdf(file)
    
    elif file_type == "docx":
        return extract_text_from_doc(file)
    
    else:
        raise ValueError("Unsupported file type")