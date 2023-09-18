#!/usr/bin/python3
"""Implementation of Base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as file_open:
            if list_objs is None:
                file_open.write("[]")
                return
            file_open.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation 'json_string'"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
