from abc import ABC, abstractmethod
#creating an abstract class for the employees 
class Employee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def calculate_bonus(self):
        pass