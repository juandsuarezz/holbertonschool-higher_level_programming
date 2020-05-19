#!/usr/bin/python3
"""Documentation of a Square class"""


class Square:
    """ Square class of a quadrilateral

    Attributes:
    __size : size of a side of the square
    """

    def __init__(self, size=0):
        """ Sets the size of the square

        Arguments:
            size (int): size of the side of the square
        """

        self.__size = size

    @property
    def size(self):
        """current size of the square

        Returns:
        size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size

        Arguments:
            value (int): new size of the square
        
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer") 

    def area(self):
        """ Finds the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
