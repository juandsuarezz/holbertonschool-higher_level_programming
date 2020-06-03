#!/usr/bin/python3
"""Documentation of a number of lines in a file function"""


def number_of_lines(filename=""):
    """Function that counts the number of lines in a file

    Arguments:
        filename (str): filename to open

    Returns:
        number of lines in the file
    """
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count = count + 1
    return count
