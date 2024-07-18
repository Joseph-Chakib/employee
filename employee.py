# employee.py
class Employee:
    used_ids = set()
    positions = ('entry', 'associate', 'director', 'partner')
    employee_count = 0
    labor_budget = 0

    def __init__(self, name='John Smith', id=0, salary=50000.0, position='entry') -> None:
        if id in Employee.used_ids or id < 0:
            raise ValueError(f"ID {id} is already taken or invalid. Please choose a different ID.")
        if position not in Employee.positions:
            raise ValueError(f"The position inputted <{position}> is not a valid position. Here is the list of valid positions: {Employee.positions}")
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position
        Employee.used_ids.add(id)
        Employee.employee_count += 1
        Employee.labor_budget += salary

    def raise_salary(self, amount):
        self.salary += amount
        Employee.labor_budget += amount

    def fire(self):
        Employee.employee_count -= 1
        Employee.labor_budget -= self.salary
        Employee.used_ids.remove(self.id)

    @classmethod
    def get_labor_budget(cls):
        return cls.labor_budget

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    def promote(self, new_position, salary_increase=0):
        if new_position not in Employee.positions:
            raise ValueError(f"The position inputted <{new_position}> is not a valid position. Here is the list of valid positions: {Employee.positions}")
        self.position = new_position
        self.raise_salary(salary_increase)

    def annual_review(self, performance_rating):
        if performance_rating > 8:
            self.raise_salary(self.salary * 0.10)  # 10% raise for high performers
        elif performance_rating > 5:
            self.raise_salary(self.salary * 0.05)  # 5% raise for average performers

    def display_info(self):
        return f"Employee Name: {self.name}, ID: {self.id}, Position: {self.position}, Salary: {self.salary}"
