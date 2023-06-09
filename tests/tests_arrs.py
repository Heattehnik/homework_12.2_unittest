import unittest
from utils.arrs import get, my_slice

class Get(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(get([], 0, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([], 0), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4], -5, -4), [])
