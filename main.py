from models.department import Department
from models.employee import Employee
from models.manager import Manager
from models.hr import HR

# Create departments
dept_sales = Department("Sales", 50000, "Alice")
dept_it = Department("IT", 100000, "Bob")

# Create employees
e1 = Employee("John Doe", "EMP001", dept_sales, 50000)
e2 = Employee("Jane Smith", "EMP002", dept_it, 60000)

# Create a manager
m1 = Manager("Mark Lee", "EMP100", dept_it, 90000)
m1.add_team_member(e1)
m1.add_team_member(e2)

# HR operations
hr = HR()
hr.add_employee(e1)
hr.add_employee(e2)
hr.add_employee(m1)

# Apply raises
e1.apply_raise()
m1.apply_raise()

# Update salary manually
hr.update_salary("EMP002", 65000)

# Generate report
hr.generate_report()

# Display total employees
print(f"\nTotal Employees: {Employee.get_total_employees()}")
