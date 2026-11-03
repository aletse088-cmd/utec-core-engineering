#!/usr/bin/env python3
"""Module that defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width: width of the rectangle (integer > 0).
            height: height of the rectangle (integer > 0).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
