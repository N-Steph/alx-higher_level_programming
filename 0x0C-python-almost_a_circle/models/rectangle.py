#!/usr/bin/python3
"""Implementation of Rectangle class"""


Base = __import__('base').Base


class Rectangle(Base):
    """Implementation of Rectangle class.
    Rectangle class inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes any new instance of the Rectangle class
        Args:
            width(int): width of Rectangle instance
            height(int): height of Rectangle instance
            x(int): rightmost position of Rectangle instance
            y(int): downward position of Rectangle instance
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for __width attribute"""
        self.__width = value

    @property
    def height(self):
        """Getter for __height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for __height attribute"""
        self.__height = value

    @property
    def x(self):
        """Getter for __x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for __x attribute"""
        self.__x = value

    @property
    def y(self):
        """Getter for __y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for __y attribute"""
        self.__y = value
