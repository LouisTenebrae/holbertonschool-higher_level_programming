#!/usr/bin/python3
"""Serialization module that adds the functionality\
    to serialize and deserialize a Python object to and from a file."""

import json

def serialize(data, filename):
    """Serialize the given object and write it to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize the object from a file."""
    with open(filename, 'r') as file:
        return json.load(file)
