#!/usr/bin/python3
"""Documentation of a JSON string function"""


import json


def to_json_string(my_obj):
    """Function that returns the JSON represntation of an object

    Arguments:
        my_obj (str): object to convert to a JSON string

    Returns:
        JSON representation of a string
    """

    return json.dumps(my_obj)
