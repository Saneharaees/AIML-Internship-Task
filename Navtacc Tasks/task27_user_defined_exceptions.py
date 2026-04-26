# Exercise on User Defined Exception Handling
class SalaryLimitError(Exception):
    """Custom exception for salary range validation"""
    def __init__(self, salary, message="Salary is not in range (10k - 50k)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

def check_salary(salary):
    if not (10000 < salary < 50000):
        raise SalaryLimitError(salary)
    else:
        print(f"Salary {salary} is approved.")

try:
    check_salary(5000)
except SalaryLimitError as e:
    print(f"Error Occurred: {e.message} | Input was: {e.salary}")
finally:
    print("Execution completed.")
