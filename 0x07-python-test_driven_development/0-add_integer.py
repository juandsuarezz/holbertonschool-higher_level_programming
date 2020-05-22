#!/usr/bin/python3
"""Documentation of a add two integers function"""


def add_integer(a, b=98):
    """Adds two integers

    Arguments:
        a (int): first int to add
        b (int): second int to add

    Returns:
        the sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        a = int(b)
    return a + b
