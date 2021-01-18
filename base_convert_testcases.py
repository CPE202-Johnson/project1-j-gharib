import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_baseError(self):
        with self.assertRaises(ValueError):  # used to check for exception
            convert(None, 1)
        
        with self.assertRaises(ValueError):  # used to check for exception
            convert(12, None)

        with self.assertRaises(ValueError):  # used to check for exception
            convert(None, 1)

        with self.assertRaises(ValueError):  # used to check for exception
            convert(-12, 1)
        with self.assertRaises(ValueError):  # used to check for exception
            convert(10, -1)
        

if __name__ == "__main__":
        unittest.main()