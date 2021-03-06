#!/usr/bin/python3
""" write a json object to a text file """


def save_to_json_file(my_obj, filename):
    """ save object to json file """

    import json
    with open(filename, mode="w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
