#!/usr/bin/python3
"""Class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Instantiation of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Method that returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """Method that returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
