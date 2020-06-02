#!/usr/bin/python3
"""Documentation of a MyInt class"""


class MyInt(int):
    """MyInt class which inherits from the int class"""

    def __init__(self, value):
        """Instantiation function

        Arguments:
            value (int): value to set the integer
        """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def __eq__(self, y):
        """Equals to operator

        Returns:
            The result of x != y
        """

        return self.value != y

    def __ne__(self, y):
        """The not equals operator

        Returns:
            The result of x == y
        """

        return self.value == y
