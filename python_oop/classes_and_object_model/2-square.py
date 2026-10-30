#!/usr/bin/env python3
"""Module that defines a class Square with a validated private size."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: size of the square (integer >= 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
