#!/usr/bin/python3
""" open and read a text file """


def read_file(filename=""):
    """ receive file name and attempt to open/read it """

    f = open(filename)
    print(f.read())
