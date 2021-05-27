#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after . ? and :
Args:
    text: input string
Returns:
    Nothing
"""


def text_indentation(text):
    """ returns string with 2 line breaks """

    if type(text) is str:
        for c in text:
            if c == '.' or c == '?' or c == ':':
                print(c)
                print()
            else:
                print(c, end='')
    else:
        raise TypeError("text must be a string")
