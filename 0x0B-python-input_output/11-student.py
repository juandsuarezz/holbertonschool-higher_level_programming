#!/usr/bin/python3
"""Documentation of a Student class"""


class Student:

    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function for Student class

        Arguments:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the instance
        Returns:
            dictionary representation of the instance
        """

        return self.__dict__
