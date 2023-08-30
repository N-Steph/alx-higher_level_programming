#!/usr/bin/python3
"""Square class module.
This module defines a class called Square with some attributes.
"""


class Square:
    """Define square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square object
        Args:
            size: size of Square object
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property position.
        Returns:
            position: position of square in cartesian plane
        """
        return self.__position

    @position.setter
    def position(self, value):
        """property setter.
        Args:
            value: new position of the Square object
        """
        if not (type(value) == tuple and
                type(value[0]) == int and
                type(value[1]) == int and
                len(value) == 2 and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of a square object
        Returns:
            self.__size ** 2: area of square of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the squaare with character #"""
        if self.__size == 0:
            print()
            return
        for pos in range(0, self.__position[1]):
            print()
        for side_1 in range(0, self.__size):
            for pos in range(0, self.__position[0]):
                print(" ", end="")
            for side_2 in range(0, self.__size):
                print("#", end="")
            print()
