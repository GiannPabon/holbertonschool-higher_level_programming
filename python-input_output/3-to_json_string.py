#!/usr/bin/python3
"""
Module that provides a function to convert a Python object into its JSON
string representation.
"""

import json


def to_json_string(my_obj):
    """
    Generates the JSON string representation of the given Python object.

    Args:
        my_obj (any): The object to be converted into a JSON string.

    Returns:
        str: A JSON-encoded string of the provided object.
    """
    return json.dumps(my_obj)
