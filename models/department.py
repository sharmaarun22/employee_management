class Department:
    def __init__(self, name, budget, head):
        self.name = name
        self.budget = budget
        self.head = head

    def __str__(self):
        return f"{self.name} (Head: {self.head}, Budget: ${self.budget})"