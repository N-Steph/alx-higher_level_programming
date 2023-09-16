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

    def test_result(self):
        """This test method tests if the correct result is outputed
        """
        self.assertEqual(max_integer([1, 2, 4, 4, 5]), 5)
        self.assertEqual(max_integer([-4, -13, 0, -5]), 0)
