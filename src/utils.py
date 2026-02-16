import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts raw text from a PDF file.
    Returns None if the file is corrupt or unreadable.
    """
    try:
        reader = PdfReader(pdf_path)
        text = "".join([page.extract_text() for page in reader.pages])
        return text
    except Exception as e:
        print(f"❌ Error reading PDF {pdf_path}: {e}")
        return None

def get_pdf_files(folder_path):
    """Returns a list of all PDF filenames in a folder."""
    return [f for f in os.listdir(folder_path) if f.endswith(".pdf")]