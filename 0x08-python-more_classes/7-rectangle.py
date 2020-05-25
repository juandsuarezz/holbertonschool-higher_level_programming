#!/usr/bin/python3
"""Documentation of a Rectangle class"""


class Rectangle:
    """Class of a rectangle"""

    print_symbol = "#"
    number_of_instances = 0

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

    def area(self):
        """Returns the area of the instance"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the instance"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Functionality for printing and using str() functions"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i is not self.__height - 1:
                rectangle.append('\n')
        return''.join(rectangle)

    def __repr__(self):
        """Creates a string that works with the eval() function"""

        string = []
        string.append("Rectangle(")
        string.append(str(self.__width) + ", " + str(self.__height) + ')')
        return ''.join(string)

    def __del__(self):
        """Functionality for when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
