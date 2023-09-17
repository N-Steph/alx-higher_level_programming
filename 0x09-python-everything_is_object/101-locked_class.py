#!/usr/bin/python3
"""This module defines a class that can accept only one predefined
attribute
"""


class LockedClass:
    """Predefining attributes for instances of a class"""
    __slots__ = ("first_name",)
