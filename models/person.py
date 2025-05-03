from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def display_details(self):
        pass
