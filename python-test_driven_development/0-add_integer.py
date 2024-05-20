#!/usr/bin/python3
"""Defining function to add 2 int"""
def add_integer(a, b=98):
    """Function to add 2 int"""
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod()
