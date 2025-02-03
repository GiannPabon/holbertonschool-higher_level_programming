#!/usr/bin/python3
"""
1. Real definition of a rectangle
A class Rectangle that defines a rectangle with width and height
"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize private instance attributes: width and height with
          validation

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the width with validation

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Property getter to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the height with validation

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
