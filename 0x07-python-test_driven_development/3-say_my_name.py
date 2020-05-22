#!/usr/bin/python3
"""Documentation of a function that prints the name and last name"""


def say_my_name(first_name, last_name=""):
    """Function that displays the first name and last name

    Arguments:
        first_name (str): first name
        last_name (str): last name
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
