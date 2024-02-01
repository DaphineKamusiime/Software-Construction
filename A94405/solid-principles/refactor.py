from abc import ABC, abstractmethod

# Single Responsibility Principle: Separating the report generation from report writing
class ReportGenerator:
    def generate_report(self, employee):
        return f"{type(employee).__name__} Report: {employee.name}"

# Interface for bonus calculation
class BonusCalculable(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass

# Bonus calculation class
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

# Employee base class following the Liskov Substitution Principle
class Employee(ABC):
    def __init__(self, name):
        self.name = name

# Manager subclass implementing BonusCalculable
class Manager(Employee, BonusCalculable):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

# Developer subclass implementing BonusCalculable
class Developer(Employee, BonusCalculable):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    report_generator = ReportGenerator()
    manager_report = report_generator.generate_report(manager)
    developer_report = report_generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(manager_report)
    print(developer_report)
    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
