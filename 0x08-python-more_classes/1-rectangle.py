#!/usr/bin/python3
"""This module defines the retangle class"""


class Rectangle:
    """Definition of the Rectangle class

    Attributes:
        width: defines the width of Rectangle object
        height: defined the height of Rectangle object
    """
    def __init__(self, width=0, height=0):
        """Initializes Rectangle object when it is creates"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines the getter of width attribute
        Returns:
            width: with of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"Defines the setter of width attribute
        Args:
          value: new width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Defines the getter of height attribute
        Returns:
            height: with of the Rectangle instance
        """
        return self.__width

    @height.setter
    def height(self, value):
        """"Defines the setter of height attribute
        Args:
          value: new height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
