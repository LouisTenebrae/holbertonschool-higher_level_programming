#!/usr/bin/python3
"""Module 0-add_integer"""


def add_integer(a, b=98):
    """
   Returns addition of the two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
