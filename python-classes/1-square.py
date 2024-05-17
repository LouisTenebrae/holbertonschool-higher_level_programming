#!/usr/bin/python3
"""Creates class Square with private attribute size and validates size"""
class Square:
     """Represents a square"""
     def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
