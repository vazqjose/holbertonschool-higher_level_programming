#!/usr/bin/python3
"""
Writes a string to a text file (UTF8)
Returns the number of characters written
"""


def write_file(filename="", text=""):
    """ receives a filename and text to insert """

    with open(filename, mode="w+", encoding="utf-8") as f:
        count = 0
        for line in text:
            count += 1
        f.write(text)
        return (count)

