from pathlib import Path

from app.extractor import extract_text_from_pdf
from app.ocr import extract_text_from_image


def extract_invoice_text(file_path):
    file = Path(file_path)

    if file.suffix.lower() == ".pdf":
        return extract_text_from_pdf(file)

    if file.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        return extract_text_from_image(file)

    raise ValueError(f"Unsupported file type: {file.suffix}")