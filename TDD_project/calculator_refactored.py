import math

class Calculator:
    # A simple calculator class.

    def add(self, x, y):
        # # Adds two numbers.
        return x + y

    def subtract(self, x, y):
        # # Subtracts y from x.
        return x - y

    def multiply(self, x, y):
        # # Multiplies two numbers.
        return x * y

    def divide(self, x, y):
        # # Divides x by y.
        if y == 0:
            return "Error: Division by zero"
        return x / y

    def exponentiate(self, x, y):
        # # Raises x to the power of y.
        return x ** y
    
    def square_root(self, x):
        # Calculates the square root of x.
        return math.sqrt(x)

    def absolute_value(self, x):
        # # Calculates the absolute value of x.
        return abs(x)
