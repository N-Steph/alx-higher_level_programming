#!/usr/bin/python3
"""This module defines the retangle class"""


class Rectangle:
    """Definition of the Rectangle class

    Attributes:
        width: defines the width of Rectangle object
        height: defined the height of Rectangle object
    """
    def __init__(self, width=0, height=0):
        """Initializes Rectangle object when it is creates
        Args:
            width (int): integer that sets the width of Rectangle instance
            height (int): integer that sets the height of Rectangle instance
        """
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
        return self.__height

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

    def area(self):
        """Calculate the area of Rectangle object
        Returns:
            area_rec : width * height
        """
        area_rec = self.__width * self.__height
        return area_rec

    def perimeter(self):
        """Evaluate the perimeter of Rectangle object
        Returns:
            perimeter: 2 * (width + height)
            0: if width or height is null
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """Defines the string representation of Rectangle Object"""
        for row in range(0, self.__height):
            for column in range(0, self.__width):
                print("#", end="")
            print()
        return ""
