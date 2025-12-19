def get_invoice(invoice_id: str) -> dict:
    # TODO: integrate with SAP/Oracle/NetSuite/etc.
    return {"invoice_id": invoice_id, "amount": 123.45, "currency": "USD"}
