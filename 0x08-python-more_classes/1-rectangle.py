#!/usr/bin/python3
"""Documentation of a Rectangle class"""


class Rectangle:
    """Class of a rectangle"""

    def __init__(self, width=0, height=0):
        """Instance of a rectangle

        Arguments:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Returns the width of the instance
        Returns:
            the width of the instance of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the instance

        Arguments:
            value (int): the width of the instance
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the instance
        Returns:
            the height of the instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the instance

        Arguments:
            value (int): the height of the instance
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
