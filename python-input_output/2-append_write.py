#!/usr/bin/python3
"""
Module that offers a function to append text to a file in UTF-8 format.
"""

def append_write(filename="", text=""):
    """
    Appends the specified string to a text file using UTF-8 encoding
    and returns the total number of characters that were added.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The string content to append.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
