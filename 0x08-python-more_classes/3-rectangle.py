o#!/usr/bin/python3
"""
Module 3-rectangle
Defines class Rectangle with private attribute size and public attribute area
"""


class Rectangle:
    """
    class Rectangle definition
    Args:
        size (int): size of a side in rectangle
    Functions:
        __init__(self, size)
        area(self)
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

    def area(self):
        """
        Calculate area of a rectangle 

        Returns:
            area
        """
       return(self._size)**2
