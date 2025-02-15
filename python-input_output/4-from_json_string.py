#!/usr/bin/python3
"""
Module that provides a function to convert a JSON string
back into its corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Deserializes a JSON-encoded string into a Python object.

    Args:
        my_str (str): A string containing valid JSON data.

    Returns:
        Any: The Python object represented by the given JSON string.
    """
    return json.loads(my_str)
