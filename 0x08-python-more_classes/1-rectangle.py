#!/usr/bin/python3
"""
Module 1-rectangle
Defines class Rectangle with private attribute size
"""


class Rectangle:
    """
    class Rectangle definition
    Args:
        size : size of a side in rectangle
    """
    def __init__(self, size):
        """
        Initializes rectangle
        Attributes:
            size: size of a side of rectangle
        """
        self.__size = size
