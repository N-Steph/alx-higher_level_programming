#!/usr/bin/python3
"""
Unit tests for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class tests the max_integr method
    """

    def test_argument(self):
        """This test method tests for the type of argument passed to
        max_integer
        """
        self.assertRaises(TypeError, max_integer, (1, 3, 4, 6, 7))
        self.assertRaises(TypeError, max_integer, {"1": 1, "3": 3, "4": 4})
        self.assertRaises(TypeError, max_integer, {1, 3, 4, 6, 7})

    def test_list_element(self):
        """This test method tests for the type of values find in the
        list passed to max_integer
        """
        self.assertRaises(TypeError, max_integer, [1, "True", 3, 98])
        self.assertRaises(TypeError, max_integer, [1, 4.1, 3, 98])
        self.assertRaises(TypeError, max_integer, [1, True, 3, 98])

    def test_result(self):
        """This test method tests if the correct result is outputed
        """
        self.assertEqual(max_integer([1, 2, 4, 4, 5]), 5)
