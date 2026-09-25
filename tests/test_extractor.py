from pathlib import Path

from app.extractor import extract_text_from_pdf


def test_extract_text_from_pdf():
    path = Path("samples/invoice.pdf")

    text = extract_text_from_pdf(path)

    assert text
    assert "ABC Supplies" in text