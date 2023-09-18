#!/usr/bin/python3
"""Implementation of Square class"""


from rectangle import Rectangle


class Square(Rectangle):
    """Square class implmentation.
    Square class inherits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize any new instance of the Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of Square intance"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "size":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def __str__(self):
        """Returns the string representation of Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
