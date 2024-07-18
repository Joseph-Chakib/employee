# main.py
from employee import Employee
from tests.test_employee import test_employee_class

# Initialize ten employees
employees = [
    Employee("Alice", 1, 60000, "associate"),
    Employee("Bob", 2, 55000, "entry"),
    Employee("Charlie", 3, 70000, "director"),
    Employee("David", 4, 50000, "entry"),
    Employee("Eve", 5, 75000, "partner"),
    Employee("Frank", 6, 62000, "associate"),
    Employee("Grace", 7, 58000, "entry"),
    Employee("Hank", 8, 72000, "director"),
    Employee("Ivy", 9, 68000, "associate"),
    Employee("Jack", 10, 52000, "entry")
]

# Display information of all employees
for emp in employees:
    print(emp.display_info())

# Run the test suite
test_employee_class()