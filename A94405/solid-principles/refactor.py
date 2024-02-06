#creating employee instances and report generation

if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    report_generator = Report()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)
