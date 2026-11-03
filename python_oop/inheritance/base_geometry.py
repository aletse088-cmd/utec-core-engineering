#!/usr/bin/env python3
"""Module that defines a class BaseGeometry."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: always, because area is not implemented here.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name: name of the value, used in the error messages.
            value: value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
