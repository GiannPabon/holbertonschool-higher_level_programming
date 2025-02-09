#!/usr/bin/python3
"""
2. Same class
A function that returns True if the object is exactly an instance of the
 specified class otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class and
    not exactly an instance of the class.

    Args:
        obj: Object to check.
        a_class: Class to check.

    Returns:
        True: if obj is an instance of a_class.
        False: if obj is not an instance of a_class.
    """
    return isinstance(obj, a_class)
