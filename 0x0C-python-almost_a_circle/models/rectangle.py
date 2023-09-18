#!/usr/bin/python3
"""Implementation of Rectangle class"""


from base import Base


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
        if value < 0:
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle instance to stdout using '#'"""
        for pos_y in range(self.__y):
            print()
        for height in range(self.__height):
            for pos_x in range(self.__x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representtion of a Rectangle instance"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
