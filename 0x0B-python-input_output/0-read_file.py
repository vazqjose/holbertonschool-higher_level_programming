#!/usr/bin/python3
""" open and read a text file """


def read_file(filename=""):
    """ receive file name and attempt to open/read it """

    with open("my_file_0.txt") as f:
        for line in f:
            print(line, end="")
