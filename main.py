import sys

from app.main import process_invoice


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run python main.py <invoice_path>")
        return

    invoice_path = sys.argv[1]

    invoice = process_invoice(invoice_path)

    print(invoice.model_dump_json(indent=2))


if __name__ == "__main__":
    main()