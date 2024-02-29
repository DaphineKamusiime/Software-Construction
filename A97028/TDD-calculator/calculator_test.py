import unittest
# Importing the Calculator class to be tested
from calculator import Calculator  

class TestCalculator(unittest.TestCase):
    # Test case to check addition functionality
    def test_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 5), 8)

    # Test case to check subtraction functionality
    def test_subtraction(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(8, 3), 5)

    # Test case to check multiplication functionality
    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 4), 8)

    # Test case to check division functionality
    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
