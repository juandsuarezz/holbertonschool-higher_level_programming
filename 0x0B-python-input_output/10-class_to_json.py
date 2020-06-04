#!/usr/bin/python3
"""Documentation of a class to json function"""


def class_to_json(obj):
    """Returns a dictionary description

    Arguments:
        obj (class object): the object to be serialized
    
    Returns:
        dictionary representation of an object
    """

    return obj.__dict__
