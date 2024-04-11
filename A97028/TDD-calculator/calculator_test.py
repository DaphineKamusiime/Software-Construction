import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        # Test addition functionality
        self.assertEqual(Calculator().add(3, 5), 8)

    def test_subtraction(self):
        # Test subtraction functionality
        self.assertEqual(Calculator().subtract(5, 3), 2)

    def test_multiplication(self):
        # Test multiplication functionality
        self.assertEqual(Calculator().multiply(3, 5), 15)

    def test_division(self):
        # Test division functionality
        self.assertEqual(Calculator().divide(10, 2), 5)
        self.assertEqual(Calculator().divide(5, 0), "Error: Division by zero")

    def test_division_by_negative_number(self):
        # Test division by negative number
        self.assertEqual(Calculator().divide(10, -2), -5)

    def test_large_numbers(self):
        # Test with large numbers
        self.assertEqual(Calculator().add(1000000, 2000000), 3000000)
        self.assertEqual(Calculator().multiply(999999, 999999), 999998000001)

    def test_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(Calculator().add(-5, 3), -2)
        self.assertEqual(Calculator().subtract(-5, -3), -2)
        self.assertEqual(Calculator().multiply(-5, 3), -15)
        self.assertEqual(Calculator().divide(-10, 2), -5)

    # additional oprations
    # exponential test function
    def test_exponentiation(self):
        calc = Calculator()
        self.assertEqual(calc.exponentiate(2, 3), 8)
        self.assertEqual(calc.exponentiate(3, 2), 9)
        self.assertEqual(calc.exponentiate(0, 5), 0)
        self.assertEqual(calc.exponentiate(5, 0), 1)

    # square root test function
    def test_square_root(self):
        calc = Calculator()
        self.assertEqual(calc.square_root(9), 3)
        self.assertEqual(calc.square_root(16), 4)
        self.assertEqual(calc.square_root(0), 0)

    # absolute value test function
    def test_absolute_value(self):
        calc = Calculator()
        self.assertEqual(calc.absolute_value(5), 5)
        self.assertEqual(calc.absolute_value(-5), 5)
        self.assertEqual(calc.absolute_value(0), 0)


if __name__ == "__main__":
    unittest.main()
