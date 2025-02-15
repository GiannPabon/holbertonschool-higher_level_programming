#!/usr/bin/python3
"""
Module that serializes a Python object to JSON format
and writes it to a specified text file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Converts a Python object into its JSON representation
    and saves this JSON string to a file.

    Args:
        my_obj (any): The object to serialize into JSON format.
        filename (str): The path to the file where the JSON
                        data will be stored.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
