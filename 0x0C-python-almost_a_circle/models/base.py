#!/usr/bin/python3
"""Implementation of Base class"""


class Base:
    """Definition of Base Class
    Args:
        __nb_object: number of instance of Base class
    """

    __nb_object = 0

    def __init__(self, id=None):
        """Initialzes an instance of the Base class.
        Args:
            id(int): identification number of the new instance created
        """
        self.__class__.__nb_object += 1
        if id is None:
            self.id = self.__class__.__nb_object
        else:
            self.id = id
