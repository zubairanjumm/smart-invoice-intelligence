from pathlib import Path

from app.extractor import extract_text_from_pdf


path = Path("samples/invoice.pdf")
text = extract_text_from_pdf(path)


def test_extract_text_from_pdf():
    assert "ABC Supplies" in text
    assert text