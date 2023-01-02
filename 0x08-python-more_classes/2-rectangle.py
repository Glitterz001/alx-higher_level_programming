#!/usr/bin/python3
"""
Module 2-Rectangle
Defines class Rectangle with private attribute size and validates size
"""


class Rectangle:
    """
    class Rectangle definition
    Args:
        size (int): size of a side in rectangle
    """

    def __init__(self, size=0):
        """
        Initializes rectangle
        Attributes:
            __size (int): size of a side of rectangle, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
