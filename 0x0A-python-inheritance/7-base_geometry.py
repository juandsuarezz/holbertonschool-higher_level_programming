#!/usr/bin/python3
"""Documentation of a BaseGeometry class"""


class BaseGeometry:

    """Base Geometry class that is empty"""

    def area(self):
        """Area function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value

        Arguments:
            name (str): string name
            value (int): value to be validated
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
