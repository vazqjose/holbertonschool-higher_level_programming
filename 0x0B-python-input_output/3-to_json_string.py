#!/usr/bin/python
""" function that returns the JSON representation of an object (string) """


import json
""" import the json module """

def to_json_string(my_obj):
    """ received a Python object as arg """

    return json.dumps(my_obj)
