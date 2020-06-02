#!/usr/bin/python3
"""Documentation of a MyList class"""


class MyList(list):
    """MyList Class"""

    def print_sorted(self):
        """Function that prints and sort a list"""

        print(sorted(self))
