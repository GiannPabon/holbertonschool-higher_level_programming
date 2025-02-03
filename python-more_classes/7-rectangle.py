#!/usr/bin/python3
"""
7. Change representation
A class Rectangle that defines a rectangle with customizable print symbol
"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize private instance attributes: width and height
          with validation
        Increments the number_of_instances during instantiation.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Public instance method that returns the rectangle area

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter

        Returns:
            int: The perimeter of the rectangle or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle using
          print_symbol

        Returns:
            str: String representation of the rectangle, or an empty string
                 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                         for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate
        a new instance using eval()

        Returns:
            str: String representation of the rectangle in the format
                 'Rectangle(width, height)'
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Detects instance deletion, prints a message, and decrements
          the instance counter"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
