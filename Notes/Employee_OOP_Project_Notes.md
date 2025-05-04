
# 🧠 Quick Interview Notes: Python OOPs Project - Employee Management System

## ✅ Project Overview
- Built a modular **Employee Management System** to practice OOP principles.
- Used abstract base classes, inheritance, encapsulation, polymorphism, magic methods, class/staticmethods, and composition.

---

## 🔁 OOP Concepts Used

### 1. **Encapsulation**
- Used private attributes (`_salary`) and `@property` decorators to manage access.
- Setter example:
```python
@salary.setter
def salary(self, value):
    if value < 0:
        raise ValueError("Salary cannot be negative")
    self._salary = value
```

### 2. **Inheritance**
- `Employee`, `Manager`, `HR` inherited from `Person`.
- Specialized behaviors via overridden methods.

### 3. **Polymorphism**
- Methods like `__str__` and `apply_raise` behave differently for `Manager`, `HR`, etc.

### 4. **Abstraction**
- `Person` was an **abstract base class** with `@abstractmethod`.

### 5. **Magic Methods**
- `__str__`: Custom string representation  
- `__eq__`, `__lt__`: For comparing employees  
- `__repr__` (if added): For debugging-friendly display

### 6. **Class & Static Methods**
- `Employee.employee_count` with `@classmethod` for tracking  
- `@staticmethod` used for utility logic not tied to instance state

### 7. **Composition**
- `Department` used inside `Employee` to model real-world relationships.

---

## 🧩 Property Setters: How They Work

- `@property` creates a getter: `employee.salary`  
- `@salary.setter` allows setting: `employee.salary = 50000`  
- You can name the property anything, but the getter/setter names **must match**

---

## ⚠️ Employee Count Design Flaw (Fixed)

**Original issue:**  
- `Employee.employee_count += 1` was in `__init__()` → count increased before employee was actually added to the system.

**Fix:**  
- Moved count increment to `HR.hire_employee()` to reflect actual hires.

---

## 📁 Project Structure

```
employee_management/
├── main.py
├── .gitignore
└── models/
    ├── __init__.py
    ├── person.py
    ├── employee.py
    ├── manager.py
    ├── hr.py
    └── department.py
```

---

## 📦 .gitignore Essentials

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/

# IDEs
.idea/
.vscode/

# OS
.DS_Store
Thumbs.db
```

🧼 **Remove already tracked ignored files:**
```bash
git rm -r --cached -f .idea/
git commit -m "Remove tracked ignored files"
```

---

## 🔧 Git Remote Setup

```bash
git remote add origin <repo-url>
git push -u origin main
```

---

## 📌 Common Errors & Fixes

| Error                        | Cause                  | Fix                                     |
|-----------------------------|------------------------|------------------------------------------|
| `CreateProcess error=2`     | Broken virtual env     | Recreate `.venv`, reconfigure interpreter|
| `Cannot push, no remote`    | Remote not added       | `git remote add origin <url>` then push |
| `.gitignore not working`    | Files already tracked  | Use `git rm --cached <file>`             |
