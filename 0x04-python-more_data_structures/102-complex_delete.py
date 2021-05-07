#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    if value is None:
        return None

    for key, val in dict(a_dictionary).items():
        if value == val:
            del a_dictionary[key]

    return a_dictionary
