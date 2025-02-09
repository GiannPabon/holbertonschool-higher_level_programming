#!/usr/bin/python3
"""
2. Same class
A function that returns True if the object is exactly an instance of the 
specified class otherwise False
""" 

def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
    class otherwise False

    Args:
        obj (object): The object to check
        a_class (class): The class to compare against

    Returns:
    bool: True if the object is exactly an instance of the specified class, 
    False otherwise 
    """
    return isinstance(obj, a_class)
