from pathlib import Path

from app.ocr import extract_text_from_image


def test_extract_text_from_image():
    path = Path("samples/test_invoice.png")

    text = extract_text_from_image(path)

    assert text
    assert "ABC Supplies" in text