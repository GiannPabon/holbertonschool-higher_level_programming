#!/usr/bin/python3
"""
10. Square #1
A class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Defines a class that inherits from Rectangle"""

    def __init__(self, size):

        """
        Initializes a Square with a given size.

        Args:
            size (int): size of the Square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not greater than 0.
        """

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
