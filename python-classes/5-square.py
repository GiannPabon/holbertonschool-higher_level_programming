#!/usr/bin/python3
"""
5. Printing a square
A class Square that defines a square and prints it with '#'
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
        self.size = size

    @property
    def size(self):
        """Property getter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set the size with validation

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Public instance method that returns the current square area

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with '#'

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
