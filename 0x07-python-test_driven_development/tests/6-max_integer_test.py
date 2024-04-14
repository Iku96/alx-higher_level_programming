#!/usr/bin/python3
# 6-max_integer_test
# Ikundwila Mwambona <ikumwana@gmail.com>
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    # Does an empty list return None?
    def test_empty_list(self):
        self.assertEqual(max_integer(list=[]), None)

    # Does the list return the max integer?
    def test_max_integer(self):
        # List contains multiple elements
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # List contains one element
        self.assertEqual(max_integer([4]), 4)
        # List with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # List with the same integers
        self.assertEqual((max_integer([4, 4, 4, 4])), 4)

    # How does the function handle Non-integer values?
    def test_non_integer(self):
        with self.assertRaises(TypeError):
            max_integer(["cat", True])
