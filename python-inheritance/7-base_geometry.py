#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Method that raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
