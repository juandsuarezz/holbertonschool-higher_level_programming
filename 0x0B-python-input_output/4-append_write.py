#!/usr/bin/python3
"""Documentation of a append to a file function"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file

    Arguments:
        filename (str): file to open
        text (str): text to append to the file
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        counter = f.write(text)
    return counter
