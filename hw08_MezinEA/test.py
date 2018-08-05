import unittest

import func from my_func

class TestFunc(unittest.TestCase):
    def test_one(self):
        val = 2
        func = func()
        self.assertEqual(func, val)