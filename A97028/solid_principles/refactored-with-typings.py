from abc import ABC, abstractmethod
from typing import Union

# Single Responsibility Principle (SRP) and Liskov Substitution Principle (LSP):
# Abstract base class defining basic attributes and method for role description
class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def role_description(self) -> str:
        pass


# Open/Closed Principle (OCP):
# Concrete subclass representing a Manager
class Manager(Employee):
    def role_description(self) -> str:
        return "Manager"

    def calculate_bonus(self) -> int:
        return 1000

    def manage_team(self) -> None:
        print(f"{self.name} is managing the team.")


# Concrete subclass representing a Developer
class Developer(Employee):
    def role_description(self) -> str:
        return "Developer"

    def calculate_bonus(self) -> int:
        return 500

    def code_review(self) -> None:
        print(f"{self.name} is conducting a code review.")


# Single Responsibility Principle (SRP):
# Class responsible for generating reports
class ReportGenerator:
    def generate_report(self, employee: Employee) -> None:
        """
        Generates a report for the given employee.
        
        Args:
            employee (Employee): An instance of an Employee subclass.
        """
        print(f"{employee.role_description()} Report: {employee.name}")


# Dependency Inversion Principle (DIP):
# Class responsible for calculating bonuses for employees
class BonusCalculator:
    def calculate_bonus(self, employee: Employee) -> int:
        """
        Calculates the bonus for the given employee.
        
        Args:
            employee (Employee): An instance of an Employee subclass.
            
        Returns:
            int: The calculated bonus amount.
        """
        return employee.calculate_bonus()


if __name__ == "__main__":
    # Creating instances of Manager and Developer
    manager = Manager("Alice")
    developer = Developer("Bob")

    # Using ReportGenerator to generate reports for employees
    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    # Using BonusCalculator to calculate bonuses for employees
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    # Printing bonuses for Manager and Developer
    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    # Executing role-specific methods for Manager and Developer
    manager.manage_team()
    developer.code_review()
