#!/usr/bin/python3
"""
3. Area of a square
A class Square that defines a square with size validation and area computation
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Define Private instance attribute: size with validation

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Public instance method that returns the current square area

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
