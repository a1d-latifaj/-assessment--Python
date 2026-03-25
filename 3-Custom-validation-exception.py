"""
    Takes salary is input
    Raises error if:
        - salary < 0
        - salary > 10000
    Otherwise returns "Valid Salary"
"""


class InvalidSalaryError(Exception):
    def __init__(self,  message="Salary is invalid"):
        self.message = message
        super().__init__(f"{message}")

def set_salary(salary):
    if salary <= 0 or salary > 10000:
        raise InvalidSalaryError(message="Salary must be between 1 and 10000")
    return "Valid salary"

try:
    salary_input = float(input("\nEnter here your salary: "))
    valid_salary = set_salary(salary_input)
    print(valid_salary)
except InvalidSalaryError as e:
    print("[ERROR]: ", e)
except ValueError:
    print("Enter a valid number")
