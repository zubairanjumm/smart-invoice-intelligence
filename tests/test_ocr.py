from app.ocr import extract_text_from_image
from pathlib  import Path

image_path = Path("samples/test_invoice.png")
text = extract_text_from_image(image_path)

def test_extract_text_from_image():
    assert text
    assert "ABC Supplies" in text

