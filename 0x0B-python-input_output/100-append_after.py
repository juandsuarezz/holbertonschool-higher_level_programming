#!/usr/bin/python3
"""Documentation of a append after function"""


def append_after(filename="", search_string="", new_string=""):
    """Function that appends a string to a text file

    Arguments:
        filename (str): file to insert a line
        search_string (str): search string
        new_string (str): new string
"""

    with open(filename, "r") as f:
        new_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
    with open(filename, "w") as f:
        f.writelines(new_list)
