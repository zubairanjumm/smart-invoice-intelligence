from app.pipeline import extract_invoice_text


def test_pdf_pipeline():
    text = extract_invoice_text("samples/invoice.pdf")

    assert text
    assert "ABC Supplies" in text


def test_image_pipeline():
    text = extract_invoice_text("samples/test_invoice.png")

    assert text
    assert "ABC Supplies" in text