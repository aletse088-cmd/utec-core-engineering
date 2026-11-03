#!/usr/bin/env python3
"""Module that defines a Square with a proper string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: size of the square (integer > 0).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
