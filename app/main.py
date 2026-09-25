from app.gemini import extract_invoice_data
from app.pipeline import extract_invoice_text


def process_invoice(file_path):
    text = extract_invoice_text(file_path)

    if not text.strip():
        raise ValueError("No text could be extracted from the invoice")

    invoice = extract_invoice_data(text)

    return invoice