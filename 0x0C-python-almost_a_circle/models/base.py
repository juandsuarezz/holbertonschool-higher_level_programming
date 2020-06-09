#!/usr/bin/python3
"""Documentation of a Base Class"""


import os
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init function"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation"""
        list_objects = []
        if list_objs is None or len(list_objs) is 0:
            list_objects = []
        else:
            for i in list_objs:
                list_objects.append(i.to_dictionary())
        json_string = Base.to_json_string(list_objects)
        with open("{}.json".format(cls.__name__), mode='w', encoding='utf-8')\
                as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            new_base = cls(1, 1)
        if cls == Square:
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename) as f:
                instance_object = cls.from_json_string(f.read())
                for instance_dict in instance_object:
                    instance_list.append(cls.create(**instance_dict))
                return instance_list
        else:
            return []
