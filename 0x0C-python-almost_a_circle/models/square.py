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

    def __str__(self):
        """Returns the string representation of Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
