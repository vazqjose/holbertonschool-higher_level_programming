#!/usr/bin/python3


"""
Class Base:
private class attribute __nb_objects = 0
"""


import json


class Base:
    """ Refer to private attr as Base.__nb_objects """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) > 0:
            return (json.dumps(list_dictionaries))
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        myList = []
        filename = cls.__name__ + ".json"
        if list_objs is not None or len(list_objs) > 0:
            for obj in list_objs:
                myList.append(cls.to_dictionary(obj))

        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            json.dump(myList, jsonfile)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
