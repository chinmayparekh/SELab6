#!/usr/bin/python3
import unittest

from If_else import factorial
from Loop import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        x = 5
        result_1 = factorial(x,y)

        n = 15
        result_2 = summation(n)

        self.assertEqual(result_1, 120)
        self.assertEqual(result_2, 120)

if __name__ == '__main__':
    unittest.main()