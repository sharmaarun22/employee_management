
# 🧩 Python OOP Project: Employee Management System

## 🎯 Objective
Design and implement a modular, real-world **Employee Management System** using **Advanced Object-Oriented Programming** concepts in Python.

---

## 🛠️ Functional Requirements

### 1. Person (Abstract Base Class)
- Common attributes: `name`, `age`, `email`
- Abstract method: `get_role()`

### 2. Employee (Inherits from Person)
- Attributes: `employee_id`, `salary`, `department`
- Methods:
  - `apply_raise()` (polymorphic behavior)
  - `__str__()`, `__eq__()`, `__lt__()` (magic methods)
- Property: `salary` with validation (no negative values)
- Class variable to track number of employees

### 3. Manager and HR (Inherit from Employee)
- **Manager** can assign tasks
- **HR** can hire employees

### 4. Department
- Attributes: `name`, `budget`, `head`
- Methods:
  - `add_employee()`
  - `get_summary()`
- Composition: Employees belong to a Department

### 5. Main Application
- Create multiple departments and employees
- Use HR to hire employees
- Use Manager to assign tasks
- Demonstrate OOP concepts through realistic interactions

---

## 📦 OOP Concepts to Implement

| Concept         | Where to Demonstrate                                         |
|----------------|---------------------------------------------------------------|
| Abstraction     | `Person` as abstract class                                    |
| Inheritance     | `Employee`, `Manager`, `HR` from `Person`                     |
| Encapsulation   | Private `_salary`, with `@property` and `@salary.setter`      |
| Polymorphism    | `apply_raise()` behaves differently in subclasses             |
| Magic Methods   | `__str__`, `__eq__()`, `__lt__()` for printing and comparisons|
| Class/Static    | `employee_count`, utility methods                             |
| Composition     | `Department` contains `Employee` instances                    |

---

## 📁 Suggested Project Structure

```
employee_management/
├── main.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── employee.py
│   ├── manager.py
│   ├── hr.py
│   └── department.py
└── Notes/
    └── Employee_OOP_Project_Notes.md
```

---

> Revisit this task to sharpen your advanced OOP skills with a real-world example!
