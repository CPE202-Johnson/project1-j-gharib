import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_06(self):
        self.assertFalse(bears(303))

    def test_bear_06(self):
        self.assertFalse(bears(300))

    def test_bear_06(self):
        self.assertFalse(bears(83))

    def test_bear_07(self):
        self.assertFalse(bears(100))

    def test_bear_error_01(self):
        with self.assertRaises(ValueError):  # used to check for exception
            bears(-1)
            
    def test_bear_error_02(self):
        with self.assertRaises(ValueError):  # used to check for exception
            bears(None)

if __name__ == "__main__":
    unittest.main()
