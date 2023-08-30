#!/usr/bin/python3
"""Square class module.
This module defines a class called Square with some attributes.
"""


class Square:
    """Define square class"""

    def __init__(self, size=0):
        """Initialize Square object
        Args:
            size: size of Square object
        """
        self.size = size

    @property
    def size(self):
        """property size. Gets the property 'size' of Square object 
        Returns:
            size: size of the Square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter. Sets the property 'size' of Square object
        Args:
            value: new value of size property
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value 

    def area(self):
        """Computes the area of a square object"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the squaare with character #"""
        if self.__size == 0:
            print()
            return
        for side_1 in range(0, self.__size):
            for side_2 in range(0, self.__size):
                print("#", end="")
            print()
