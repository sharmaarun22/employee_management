from .person import Person
from .department import Department

class Employee(Person):
    _employee_count = 0

    def __init__(self, name, emp_id, department: Department, salary):
        super().__init__(name, emp_id)
        self._salary = salary
        self.department = department
        Employee._employee_count += 1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def apply_raise(self):
        self.salary *= 1.05

    def display_details(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}, Salary: {self.salary}, Dept: {self.department.name}")

    @classmethod
    def get_total_employees(cls):
        return cls._employee_count

    @staticmethod
    def validate_employee_id(emp_id):
        return str(emp_id).startswith("EMP")

    def __str__(self):
        return f"{self.name} ({self.emp_id})"

    def __eq__(self, other):
        return self.emp_id == other.emp_id

    def __lt__(self, other):
        return self.salary < other.salary