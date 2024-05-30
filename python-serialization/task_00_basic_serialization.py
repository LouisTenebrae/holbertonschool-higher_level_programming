#!/usr/bin/python3
"""Serialization module """
import json

def serialize_and_save_to_file(data, filename):
    """Serialize the given object and write it to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize the object from a file."""
    with open(filename, 'r') as file:
        return json.load(file)
