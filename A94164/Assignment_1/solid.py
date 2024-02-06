from abc import ABC, abstractmethod

# Base Employee class with abstract methods
class Employee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def calculate_bonus(self):
        """Calculate bonus for an employee."""
        pass

    @abstractmethod
    def generate_report(self):
        """Generate a report for an employee."""
        pass

# Manager class inheriting from Employee
class Manager(Employee):
    def calculate_bonus(self):
        # Specific bonus calculation for Manager
        return 1000

    def generate_report(self):
        # Specific report generation for Manager
        print(f"Manager Report: {self.name}")

    def manage_team(self):
        # Additional responsibility specific to Manager
        print(f"{self.name} is managing the team.")

# Developer class inheriting from Employee
class Developer(Employee):
    def calculate_bonus(self):
        # Specific bonus calculation for Developer
        return 500

    def generate_report(self):
        # Specific report generation for Developer
        print(f"Developer Report: {self.name}")

    def code_review(self):
        # Additional responsibility specific to Developer
        print(f"{self.name} is conducting a code review.")

# Main execution block
if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    employees = [manager, developer]

    # Loop through each employee to generate reports and calculate bonuses
    for employee in employees:
        employee.generate_report()  # Polymorphic call to generate report
        bonus = employee.calculate_bonus()
        print(f"{employee.role} Bonus: ${bonus}")

    # Executing role-specific behaviors
    manager.manage_team()
    developer.code_review()


