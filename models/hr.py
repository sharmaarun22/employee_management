from .employee import Employee

class HR:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        if not isinstance(emp, Employee):
            raise ValueError("Only Employee instances can be added")
        self.employees.append(emp)
        Employee.employee_count += 1

    def remove_employee(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]

    def update_salary(self, emp_id, new_salary):
        for e in self.employees:
            if e.emp_id == emp_id:
                e.salary = new_salary
                break

    def generate_report(self):
        print("\nEmployee Report:")
        for e in self.employees:
            e.display_details()
