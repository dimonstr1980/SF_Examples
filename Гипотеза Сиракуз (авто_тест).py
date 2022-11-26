import unittest
from main import check_h


class basicTest(unittest.TestCase):
    def test_ok(self):
        self.assertTrue(check_h(10))
        self.assertTrue(check_h(15))
        self.assertTrue(check_h(3))

if __name__ == '__main__':
    unittest.main()
