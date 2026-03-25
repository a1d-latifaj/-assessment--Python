"""
    Validate:
        - id must not be None
        - name must not be empty
        - salary must be positive
    
    Return:
        - invalid records
        - reason for each issue
"""

employees = [
    {"id": 1, "name":"Alice", "salary":700},
    {"id": 2, "name":"", "salary":500},
    {"id": 3, "name":"Bob", "salary":-200},
    {"id": None, "name":"Eve", "salary":900},
]

invalid_records = []

for employee in employees:
    reasons = []

    if employee['id'] is None:
        reasons.append("ID must not be empty")

    if employee['name'] == '':
        reasons.append("Name must not be empty")

    if employee['salary'] <= 0:
        reasons.append("Salary must not be negative")

    if reasons:
        invalid_records.append(
            {
            "employee": employee,
            "reasons": reasons
        })


for inv in invalid_records:
    print(f"RECORD: {inv['employee']}")
    print(f"REASON: {inv['reasons'][0]}\n")