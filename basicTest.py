import unittest
from Root.src.main import is_leap_year # /root/src/main.py


class basicTest(unittest.TestCase):
    def test_leap(self):
        self.assertTrue(is_leap_year(2000))

    def test_not_leap(self):
        self.assertFalse(is_leap_year(2001))

if __name__ == '__main__':
    unittest.main()