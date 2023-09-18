#!/usr/bin/python3
"""Implementation of the unit test for Base class"""


import unittest
from models.base import Base


class TestBase:
    """Implementation of Base class unit tests"""
    def setUp(self):
        """Initialization for the unit tests"""
        b1 = Base()
        b2 = Base(1993)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1993)
