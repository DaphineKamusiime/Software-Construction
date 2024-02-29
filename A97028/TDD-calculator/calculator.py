class Calculator:
    # Method to perform addition
    def add(self, a, b):
        return a + b

    # Method to perform subtraction
    def subtract(self, a, b):
        return a - b

    # Method to perform multiplication
    def multiply(self, a, b):
        return a * b

    # Method to perform division
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
