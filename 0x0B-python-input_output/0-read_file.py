#!/usr/bin/python3
"""Documentation of a read file function"""


def read_file(filename=""):
    """Function that reads the file and prints his content

    Arguments:
        filename (str): filename to open
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
