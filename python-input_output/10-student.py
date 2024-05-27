#!/usr/bin/python3
""" Student module"""


class Student:
    """ Student class"""

    def __init__(self, first_name, last_name, age):
        """ Initializes a student instance"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name


    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in attrs:
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict
