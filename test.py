import unittest

from prog1 import factorial
from prog2 import summation
class TestFact(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to check factorial of numbers
        """
        x = 5
        result_1 = factorial(x)

        n = 10
        result_2 = summation(n)

        self.assertEqual(result_1, 120)
        self.assertEqual(result_2, 55)

if __name__ == '__main__':
    unittest.main()