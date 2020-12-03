from modules.calculator import *

import unittest

class TestCalculator(unittest.TestCase):
    def setUp():
        self.num1 = 8
        self.num2 = 2

    def test_addition(self):
        addition = add(self.num1, self.num2)
        self.assertEqual(10, addition)

    def test_subtraction(self):
        subtraction = subtract(self.num1, self.num2):
        self.assertEqual(6, subtraction)


