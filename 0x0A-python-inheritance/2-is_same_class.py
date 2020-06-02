#!/usr/bin/python3
"""Documentation of a class instance checker"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance

    Returns:
        True if object is an instance, False otherwise
    """

    if type(obj) == a_class:
        return True
    else:
        return False
