#!/usr/bin/python3
"""
0. Lookup
A function that returns the list of available attributes and methods
 of an object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    Args:
        obj (object): The object whose attributes and methods need to be
        looked up.

    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
