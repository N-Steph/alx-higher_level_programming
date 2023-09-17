#!/usr/bin/python3
"""Implementation of MyInt class that inherits from int"""


class MyInt(int):
    """MyInt class inherits from int class.
    MyInt revers the operators == and !=
    """
    def __eq__(self, obj):
        """Returns False if two MyInt instances have the same values"""
        return super().__ne__(obj)

    def __ne__(self, obj):
        """Returns True if two MyInt instances have different values"""
        return super().__eq__(obj)
