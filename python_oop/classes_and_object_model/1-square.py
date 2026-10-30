#!/usr/bin/env python3
"""Module that defines a class Square with a private size."""


class Square:
    """Class that represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: size of the square, stored as a private attribute.
        """
        self.__size = size
