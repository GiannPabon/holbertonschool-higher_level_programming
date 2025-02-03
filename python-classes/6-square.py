#!/usr/bin/python3
"""
6. Coordinates of a square
A class Square that defines a square with size and position
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Define Private instance attributes: size and position with
           validation

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a
            tuple of 2 positive integers.

            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Property getter to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter to set the position with validation

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Public instance method that returns the current square area

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with '#' considering
          the position

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
