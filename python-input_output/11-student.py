#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance"""
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key in json:
            setattr(self, key, json[key])
