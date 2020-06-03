#!/usr/bin/python3
"""Documentation of a write file function"""


def write_file(filename="", text=""):
    """Writes a specified text to a file

    Arguments:
        filename (str): file to open
        text (str): text to write to the file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        counter = f.write(text)
    return counter
