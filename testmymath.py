import mymath
import unittest

class TestMyMath(unittest.TestCase):

    def test_sum_one_and_one(self):
        result = mymath.sum(1,1)
        self.assertEqual(result,2)

unittest.main()
