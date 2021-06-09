#!/usr/bin/python3


"""
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None):
    * if id is not None, assign the public instance attribute id with
    this argument value - you can assume id is an integer and you don’t
    need to test the type of it otherwise, increment __nb_objects and 
    assign the new value to the public instance attribute id

    * This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to 
    avoid duplicating the same code (by extension, same bugs)
"""


import json


class Base:
    """ Refer to private attr as Base.__nb_objects """

    __nb_objects = 0

    def __init__(self, id=None):

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

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

