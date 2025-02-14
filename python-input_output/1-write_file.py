#!/usr/bin/python3
"""
Module that overwrites the content of a file
with a given string in UTF-8.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number
    of characters that were written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
