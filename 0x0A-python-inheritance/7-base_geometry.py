#!/usr/bin/python3
"""Defining the BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with its method"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises an exception base on the type and value of 'value'
        Raises of TypeError exception if 'value' is not an integer
        Raises a ValueError exception if 'value' is less than or equal 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
