# tests/test_employee.py
import sys
import os

# Add the parent directory to the sys.path to import employee module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from employee import Employee

def test_employee_class():
    try:
        # Test unique ID constraint
        emp = Employee("Test", 1, 50000, "entry")
    except ValueError as e:
        print(f"Test Passed: {e}")

    try:
        # Test valid position constraint
        emp = Employee("Test", 11, 50000, "invalid_position")
    except ValueError as e:
        print(f"Test Passed: {e}")

    # Test raise salary
    emp = Employee("Test Raise", 11, 50000, "entry")
    emp.raise_salary(5000)
    assert emp.salary == 55000, "Test Failed: Raise Salary"
    print("Test Passed: Raise Salary")

    # Test fire employee
    emp.fire()
    assert Employee.employee_count == 10, "Test Failed: Fire Employee"
    assert Employee.labor_budget == sum(e.salary for e in employees), "Test Failed: Labor Budget After Fire"
    print("Test Passed: Fire Employee")

    # Test labor budget and employee count
    assert Employee.get_labor_budget() == sum(e.salary for e in employees), "Test Failed: Get Labor Budget"
    assert Employee.get_employee_count() == 10, "Test Failed: Get Employee Count"
    print("Test Passed: Get Labor Budget and Employee Count")

    # Test promotion
    emp = Employee("Test Promote", 12, 50000, "entry")
    emp.promote("associate", 5000)
    assert emp.position == "associate", "Test Failed: Promote Employee"
    assert emp.salary == 55000, "Test Failed: Salary After Promotion"
    print("Test Passed: Promote Employee")

    # Test annual review
    emp.annual_review(9)
    assert emp.salary == 60500, "Test Failed: Annual Review High Performer"
    print("Test Passed: Annual Review High Performer")

    emp.annual_review(6)
    assert emp.salary == 63525, "Test Failed: Annual Review Average Performer"
    print("Test Passed: Annual Review Average Performer")

if __name__ == "__main__":
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

    test_employee_class()