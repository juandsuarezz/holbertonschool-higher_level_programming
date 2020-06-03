#!/usr/bin/python3
"""Documentation of a JSON string to object"""


import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string

    Arguments:
        my_str (str): string to encode JSON
    """

    return json.loads(my_str)
