#!/usr/bin/python3
"""Module that defines a class Rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """__init__ method that sets the intance with a width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Method that returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method that sets the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Method that returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that sets the value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Method that returns the area of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Method that returns a string representation of the instance"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for i in range(self.height)])

    def __repr__(self):
        """Method that returns the string representation of the instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when an instance is deleted"""
        print("Bye rectangle...")
