#!/usr/bin/python3
"""This module contains the Rectangle class definition"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition.
    Rectangle class inherits from the BaseGeometry class
    """

    def __init__(self, width, height):
        """Intialize a Rectangle instance
        Args:
            self.__width: instance attribute, width of Rectangle instance
            self.__height: instance attribue, height of Rectangle instance
        """
        data = {'width': width, 'height': height}
        for key, value in data.items():
            super().integer_validator(key, value)
        self.__width = width
        self.__height = height
