import unittest
from io import StringIO
from unittest.mock import patch

def custom_input(_in):
    def wrapped(ignored):
        return _in
    return wrapped

class dictTest(unittest.TestCase):
    def test_runs(self):
        with patch('builtins.input', new=custom_input('123')) as new_input:
            from Root.src import main

if __name__ == '__main__':
    unittest.main()
