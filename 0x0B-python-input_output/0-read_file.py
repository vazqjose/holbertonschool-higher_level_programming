#!/usr/bin/python3
""" open and read a text file as parameter """


def read_file(filename=""):
    """ receive file name and attempt to open/read it """

    with open(filename) as f:
        for line in f:
            print(line, end="")
