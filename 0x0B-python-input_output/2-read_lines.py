#!/usr/bin/python3
"""Documentation of a Read n lines function"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file

    Arguments:
        filename (str): filename to open
        nb_lines (int): number of lines to print
    """

    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
