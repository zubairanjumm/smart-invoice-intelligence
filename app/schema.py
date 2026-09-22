from datetime import date
from pydantic import BaseModel
from typing import List


class InvoiceItem(BaseModel):
    description: str
    quantity: float
    unit_price: float
    amount: float


class Invoice(BaseModel):
    vendor_name: str
    invoice_number: str
    invoice_date: date
    due_date: date
    currency: str
    subtotal: float
    tax: float
    total: float
    items: List[InvoiceItem]