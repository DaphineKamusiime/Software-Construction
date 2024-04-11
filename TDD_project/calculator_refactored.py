import math

class Calculator:
    """
    A simple calculator class for basic arithmetic operations, exponentiation, square root, and absolute value calculation.
    """

    def add(self, x, y):
        """
        Adds two numbers.
        :param x: First number.
        :param y: Second number.
        :return: The sum of x and y.
        """
        return x + y

    def subtract(self, x, y):
        """
        Subtracts y from x.
        :param x: First number.
        :param y: Second number to be subtracted from x.
        :return: The difference of x and y.
        """
        return x - y

    def multiply(self, x, y):
        """
        Multiplies two numbers.
        :param x: First number.
        :param y: Second number.
        :return: The product of x and y.
        """
        return x * y

    def divide(self, x, y):
        """
        Divides x by y.
        :param x: Numerator.
        :param y: Denominator.
        :return: The quotient of x and y if y is not zero, otherwise raises a ZeroDivisionError.
        """
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y

    def exponentiate(self, x, y):
        """
        Raises x to the power of y.
        :param x: Base.
        :param y: Exponent.
        :return: x raised to the power of y.
        """
        return x ** y

    def square_root(self, x):
        """
        Calculates the square root of x.
        :param x: The number to find the square root of.
        :return: The square root of x. If x is negative, it raises a ValueError.
        """
        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(x)

    def absolute_value(self, x):
        """
        Calculates the absolute value of x.
        :param x: The number to find the absolute value of.
        :return: The absolute value of x.
        """
        return abs(x)

