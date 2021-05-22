#!/usr/bin/python3
"""
Function that prints My name is <first name> <last name>

Args:
    first_name: first name
    last_name: the last name

Returns:
    Nothing
"""


def say_my_name(first_name, last_name=""):
    """ Function will print a full name """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
