import unittest
from utils.arrs import get, my_slice

class Get(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([], 0, "test"), "test")
