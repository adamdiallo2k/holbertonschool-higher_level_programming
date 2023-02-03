#!/usr/bin/python3
"""Module to find the max integer in a list
"""

import unittest

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        # Test with an empty list
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        # Test with a list of mixed integers
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_non_integer_elements(self):
        # Test with a list containing non-integer elements
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4, 5])

if __name__ == '__main__':
    unittest.main()
