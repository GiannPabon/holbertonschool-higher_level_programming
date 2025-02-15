#!/usr/bin/python3
"""
This module defines a function that generates a dictionary of an object's
attributes suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Creates a JSON-serializable dictionary from the __dict__ attribute
    of the given object.

    Args:
        obj (object): The instance whose attributes will be converted.

    Returns:
        dict: A dictionary representing the object's attributes,
              ready for JSON serialization.
    """
    return obj.__dict__
