#!/usr/bin/python3
"""Documentation of a function that print a square"""


def print_square(size):
    """Function that print a square of length size

    Arguments:
        size (int): the side length of the square
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
