#!/usr/bin/python3
"""Documentation of a load from json file function"""


import json


def load_from_json_file(filename):
    """creates an object from a json file

    Arguments:
        filename (str): file to load the string

    Returns:
        JSON object represented by the string
    """

    with open(filename) as f:
        json_obj = json.load(f)
    return json_obj
