#!/usr/bin/python3
def print_last_digit(number):
    absnumber = abs(number)
    lastdigit = absnumber % 10

    if number < 0:
        lastdigit = lastdigit * -1

    return lastdigit
