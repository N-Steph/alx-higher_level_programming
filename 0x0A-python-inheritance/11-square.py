#!/usr/bin/python3
"""Implementation of the Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class implementation
    Square class inherits from Rectangle class which iself inherits\
     from the BaseGeometry class
    Here we have a case of multi inheritance
    """

    def __init__(self, size):
        """Initialze the Square instance.
        self.__size: instance variable, size of the square
        """
        self.__size = size

    def area(self):
        """Returns the area of a Square instance"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)
