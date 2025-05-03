from .employee import Employee

class Manager(Employee):
    def __init__(self, name, emp_id, department, salary):
        super().__init__(name, emp_id, department, salary)
        self.team = []

    def add_team_member(self, emp):
        self.team.append(emp)

    def apply_raise(self):
        self.salary *= 1.10

    def display_details(self):
        super().display_details()
        print(f"Manages: {[e.name for e in self.team]}")