#!/usr/bin/python3
"""
2. Same class
A function that returns True if the object is exactly an instance of
the specified class otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is instance of given class.
    Otherwise, returns False.
    Args:
        obj: Object to check.
        a_class: Given class.
    Returns:
        True: if obj is an exact instance of a_class.
        False: if obj is not exactly an instance.
    """
    return isinstance(obj, a_class)
