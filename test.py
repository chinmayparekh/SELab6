#!/usr/bin/python3
import unittest

from Fact import factorial
from Sum import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        a = 5
        result_1 = factorial(a) # 120

        b = 6
        result_2 = factorial(b) #720

        c= 2
        result_3 = factorial(c) #2

        n = 15
        result_4 = summation(n) #120

        m = 10
        result_5 = summation(m) #55

        # self.assertEqual(result_1, 120)
        # self.assertEqual(result_2, 720)
        # self.assertEqual(result_3, 20) #fail
        # self.assertEqual(result_4, 120)
        self.assertEqual(result_5, 50) #fail



if __name__ == '__main__':
    unittest.main()