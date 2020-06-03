#!/usr/bin/python3
"""Documentation of a save object to a file function"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file

    Arguments:
        my_obj (str): text to write in a file
        filename (str): file to write
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
