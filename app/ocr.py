from pathlib import Path

from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):
    image = Path(image_path)
    pill_image = Image.open(image)

    text = pytesseract.image_to_string(pill_image)

    return text