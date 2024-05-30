#!/usr/bin/python3
"""Pickle"""
import pickle

class CustomObject:
    """Custom object"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object"""
        print("Name: {self.name}, Age: {self.age}, Is student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and write it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None
    
    @classmethod
    def deserialize(cls, filename):
        """Load and deserialize the object from a file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
