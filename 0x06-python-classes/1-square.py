#!/usr/bin/python3
"""Documentation of a square class"""


class Square:
    """Square class of a quadrilateral

    Attributes:
    __size: size of a side
    """
    def __init__(self, size):
        """ Initial size

        Arguments:
            size (int): size of a side of the square
        """
        self.__size = size
