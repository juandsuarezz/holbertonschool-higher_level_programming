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

    @property
    def position(self):
        """ get the position

        Returns: The position of the square 
        """
        return self.__position

    @position.setter
    def position(self):
        """sets the position

        Arguments:
            value (tuple): position of the square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Finds the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square"""

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))
            
