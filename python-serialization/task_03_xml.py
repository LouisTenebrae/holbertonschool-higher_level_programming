#!/usr/bin/python3
"""XML"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize the given object and write it to a file."""
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load and deserialize the object from a file."""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
