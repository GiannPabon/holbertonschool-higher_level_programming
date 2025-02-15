#!/usr/bin/python3
"""
Module that restores a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns its data as a Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        Any: The Python object derived from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
