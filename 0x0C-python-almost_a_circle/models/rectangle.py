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
        args = {"width": width, "height": height, "x": x, "y": y}
        for key, value in args.items():
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(key))

        args1 = {"width": width, "height": height}
        for key, value in args1.items():
            if value <= 0:
                raise ValueError("{} must be > 0".format(key))

        args2 = {"x": x, "y": y}
        for key, value in args2.items():
            if value < 0:
                raise ValueError("{} must be >= 0".format(key))

        super().__init__(id)
        self.__width = width 
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for __width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for __height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for __height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for __x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for __x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for __y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for __y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
