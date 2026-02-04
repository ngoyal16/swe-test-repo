import unittest
from calculator import add, subtract, multiply, divide, modulo

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Cannot divide by zero.")

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10.5, 3), 1.5)
        with self.assertRaises(ValueError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
