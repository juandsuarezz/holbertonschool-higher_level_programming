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


class Rectangle(BaseGeometry):

    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation function

        Arguments:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area function
        Returns:
            The area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """The function for use in print() and str()
        Returns:
            Specially formated string
        """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
