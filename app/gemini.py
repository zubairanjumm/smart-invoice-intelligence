import os

from dotenv import load_dotenv
from google import genai

from app.schema import Invoice


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)


def extract_invoice_data(text):
    prompt = f"""
Extract the invoice information from the following text.

Return only the information that is actually present in the invoice.
Do not invent missing values.

Invoice text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Invoice,
        },
    )

    return response.parsed