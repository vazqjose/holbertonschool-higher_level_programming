#!/usr/bin/python3
def text_indentation(text):
    if type(text) is str:
        for c in text:
            if c == '.' or c == '?' or c == ':':
                print(c)
                print()
            else:
                print(c, end='')
    else:
        raise TypeError("text must be a string")
