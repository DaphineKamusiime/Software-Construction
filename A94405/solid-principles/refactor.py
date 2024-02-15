from abc import ABC, abstractmethod

# Step 1: Create Abstract Base Class for Employee
class Employee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_bonus(self):
        pass

# Step 2: Create Abstract Base Class for Report Generation
class ReportGenerator(ABC):
    def generate_report(self, employee):
        pass

# Step 3: Implement Report Generation Class
class Report(ReportGenerator):
    def generate_report(self, employee):
        if isinstance(employee, Manager):
            self.write_manager_report(employee)
        elif isinstance(employee, Developer):
            self.write_developer_report(employee)

    def write_manager_report(self, manager):
        print(f"Manager Report: {manager.name}")

    def write_developer_report(self, developer):
        print(f"Developer Report: {developer.name}")

# Step 4: Implement BonusCalculator Class
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

# Step 5: Implement Manager Class with Bonus Calculation
class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

# Step 6: Implement Developer Class with Bonus Calculation
class Developer(Employee):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

# Step 7: Create Employee Instances and Generate Reports
if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = Report()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

# Step 8: Calculate Bonuses using BonusCalculator
if __name__ == "__main__":
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

# Step 9: Manager Specific Functionality
if __name__ == "__main__":
    manager.manage_team()

# Step 10: Developer Specific Functionality
if __name__ == "__main__":
    developer.code_review()
