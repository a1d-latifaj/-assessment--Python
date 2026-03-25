"""
    Requirements:
      Write a function that:
        1: Calculate total amount for each invoice (just use amount here)
        2: Return only valid invoices

    Conditions:
        1: Amount must be positive
        2: Status must be 'paid'
"""

invoices = [
    {"invoice_id": 1, "amount":150, "status":"paid"},
    {"invoice_id": 2, "amount":-30, "status":"paid"},
    {"invoice_id": 3, "amount":200, "status":"pending"},
    {"invoice_id": 4, "amount":100, "status":"paid"},
]
            
def invoice_processing(list_of_invoices):
    valid_invoices = []
    total = 0
    for inv in list_of_invoices:
        if inv['amount'] > 0 and inv['status'] == 'paid':
            valid_invoices.append(inv)
            total += inv['amount']

    return valid_invoices, total

valid_invoices, total = invoice_processing(invoices)

print("Valid Invoices:")
for inv in valid_invoices:
    print(f"  {inv['invoice_id']}: amount: {inv['amount']}, Status: {inv['status']}")
print(f"Total Amount: {total}")

