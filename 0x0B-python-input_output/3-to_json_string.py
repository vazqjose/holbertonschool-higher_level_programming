#!/usr/bin/python3
""" function that returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    """ received a Python object as arg """

    import json
    return json.dumps(my_obj)
