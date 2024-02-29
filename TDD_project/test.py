# tests/test_calculator.py

import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Test addition of two positive numbers
        self.assertEqual(add(3, 5), 8)

    def test_add_positive_and_negative_numbers(self):
        # Test addition of positive and negative numbers
        self.assertEqual(add(-1, 1), 0)

    def test_add_negative_numbers(self):
        # Test addition of two negative numbers
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        # Test addition with zero
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -1), -1)
        self.assertEqual(add(0, 0), 0)

    def test_add_large_numbers(self):
        # Test addition of large numbers
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_subtract_positive_numbers(self):
        # Test subtraction of positive numbers
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_positive_and_negative_numbers(self):
        # Test subtraction of positive and negative numbers
        self.assertEqual(subtract(1, -1), 2)

    def test_subtract_negative_numbers(self):
        # Test subtraction of two negative numbers
        self.assertEqual(subtract(-1, -1), 0)

    def test_subtract_zero(self):
        # Test subtraction with zero
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, -1), 1)
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_large_numbers(self):
        # Test subtraction of large numbers
        self.assertEqual(subtract(2000000, 1000000), 1000000)

if __name__ == '__main__':
    unittest.main()
