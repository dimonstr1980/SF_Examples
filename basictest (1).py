import unittest
from main import are_both_odd


class basicTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(are_both_odd(21, 23))

    def test_false(self):
        self.assertFalse(are_both_odd(2, 4))

if __name__ == '__main__':
    unittest.main()
