import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    pdf = Path(pdf_path)

    with pymupdf.open(pdf) as document:
        combined_text = ""

        for page in document:
            combined_text += page.get_text()

    return combined_text


