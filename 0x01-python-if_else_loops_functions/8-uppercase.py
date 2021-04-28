#!/usr/bin/python3
def uppercase(str):
    for char in str:
        myInt = ord(char)
        if char.islower():
            myInt = myInt - 32
        print('{:c}'.format(myInt), end='')
    print()
