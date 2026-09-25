# Smart Invoice Intelligence

An AI-powered invoice processing pipeline that extracts structured information from PDF and image invoices, validates the extracted data with Pydantic, and returns clean JSON.

Built as **Project 1 of my 30 Days → 30 AI Projects challenge**.

## Overview

Invoices usually contain useful information in an unstructured format:

* Vendor information
* Invoice numbers
* Dates
* Items
* Quantities
* Prices
* Taxes
* Totals
* Currency

This project converts that unstructured invoice content into structured, validated data.

```text
Invoice PDF / Image
        ↓
   File Detection
        ↓
 ┌──────┴──────┐
 ↓             ↓
PyMuPDF     Tesseract OCR
 ↓             ↓
 └──────┬──────┘
        ↓
   Extracted Text
        ↓
      Gemini
        ↓
 Structured Invoice
        ↓
    Pydantic
        ↓
  Validated JSON
        ↓
   Streamlit GUI
```

## Features

* PDF text extraction with **PyMuPDF**
* Image OCR with **Tesseract**
* AI-powered invoice information extraction with **Gemini**
* Structured output using **Pydantic**
* Automatic validation of extracted invoice data
* Support for:

  * PDF
  * PNG
  * JPG
  * JPEG
* Command-line interface
* Streamlit testing interface
* Unit tests for extraction and pipeline components

## Extracted Data

The system currently extracts:

```json
{
  "vendor_name": "ABC Supplies",
  "invoice_number": "INV-001",
  "invoice_date": "2026-09-23",
  "due_date": "2026-10-23",
  "currency": "USD",
  "subtotal": 125.0,
  "tax": 12.5,
  "total": 137.5,
  "items": [
    {
      "description": "Keyboard",
      "quantity": 2,
      "unit_price": 50.0,
      "amount": 100.0
    },
    {
      "description": "Mouse",
      "quantity": 1,
      "unit_price": 25.0,
      "amount": 25.0
    }
  ]
}
```

## Project Structure

```text
smart-invoice-intelligence/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schema.py
│   ├── extractor.py
│   ├── ocr.py
│   ├── pipeline.py
│   ├── gemini.py
│   └── streamlit_app.py
│
├── tests/
│   ├── __init__.py
│   ├── test_extractor.py
│   ├── test_ocr.py
│   ├── test_pipeline.py
│   └── test_gemini.py
│
├── samples/
│   ├── invoice.pdf
│   └── test_invoice.png
│
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── main.py
```

## Tech Stack

| Technology    | Purpose                               |
| ------------- | ------------------------------------- |
| Python        | Core application                      |
| PyMuPDF       | PDF text extraction                   |
| Tesseract OCR | Image text extraction                 |
| Pillow        | Image processing                      |
| Gemini API    | Invoice information extraction        |
| Pydantic      | Data validation and schemas           |
| Streamlit     | Testing interface                     |
| pytest        | Automated testing                     |
| uv            | Dependency and environment management |

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/zubairanjumm/smart-invoice-intelligence.git
cd smart-invoice-intelligence
```

### 2. Create the virtual environment

```bash
uv venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Configure the Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your `.env` file.

## OCR Requirement

Image invoices use Tesseract OCR.

On Windows, install Tesseract and make sure the executable is available at the path configured in `app/ocr.py`.

Example:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

## Run the CLI

Process an invoice from the command line:

```powershell
uv run python main.py samples/invoice.pdf
```

For an image:

```powershell
uv run python main.py samples/test_invoice.png
```

The extracted invoice will be printed as structured JSON.

## Run the Streamlit Interface

Start the GUI:

```powershell
uv run python -m streamlit run app/streamlit_app.py
```

Then open the local Streamlit URL shown in the terminal.

Upload either:

```text
samples/invoice.pdf
```

or:

```text
samples/test_invoice.png
```

and click **Extract Invoice**.

## Run Tests

Run the complete test suite:

```powershell
uv run pytest
```

The tests cover:

* PDF extraction
* OCR extraction
* File-type pipeline
* Gemini invoice extraction

## How It Works

### 1. File Detection

The pipeline checks the uploaded file extension.

```text
.pdf → PyMuPDF
.png/.jpg/.jpeg → Tesseract OCR
```

### 2. Text Extraction

For PDFs containing selectable text, PyMuPDF extracts the text directly.

For image invoices, Tesseract converts the image into text.

### 3. AI Extraction

The extracted text is sent to Gemini with the `Invoice` Pydantic schema.

Gemini maps the unstructured text into the expected invoice structure.

### 4. Validation

Pydantic validates the returned structure and data types.

For example:

```text
quantity → float
unit_price → float
total → float
invoice_date → date
items → List[InvoiceItem]
```

### 5. JSON Output

The validated invoice object can then be serialized into JSON for further processing.

## Current Limitations

This is a learning project and is not intended to be production-ready.

Current limitations include:

* OCR accuracy depends on image quality
* Invoice layouts vary significantly
* Different date and currency formats may require additional handling
* Missing fields are not yet handled with sophisticated fallback logic
* The system currently relies on an external Gemini API
* Tesseract requires a local installation for image processing
* The Streamlit interface is primarily for testing the pipeline

## Future Improvements

Potential improvements include:

* Better OCR preprocessing
* Support for more invoice layouts
* More robust handling of missing fields
* Confidence scoring
* Invoice validation rules
* Better error handling
* Batch invoice processing
* Improved Streamlit interface
* More comprehensive test invoices
* Support for additional document formats
* Local/alternative AI models

## Learning Goals

This project is part of my **30 Days → 30 AI Projects** challenge.

The goal is not just to build a working application, but to practice building complete AI pipelines involving:

* Document processing
* OCR
* LLM integration
* Structured outputs
* Pydantic validation
* Testing
* CLI applications
* Simple interfaces
* End-to-end system design

## Author

**Zubair Anjum**

GitHub: [zubairanjumm](https://github.com/zubairanjumm)

---

**Project 1 / 30 — Smart Invoice Intelligence**
