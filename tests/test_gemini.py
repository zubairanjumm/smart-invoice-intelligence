from app.extractor import extract_text_from_pdf
from app.gemini import extract_invoice_data


def test_extract_invoice_data():
    text = extract_text_from_pdf("samples/invoice.pdf")

    invoice = extract_invoice_data(text)

    assert invoice.vendor_name == "ABC Supplies"
    assert invoice.invoice_number == "INV-001"
    assert invoice.total == 137.50
    assert len(invoice.items) == 2