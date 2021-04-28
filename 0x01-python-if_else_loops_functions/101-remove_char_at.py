#!/usr/bin/python3
def remove_char_at(str, n):
    myStr = ''
    for myIndex in range(0, len(str)):
        if myIndex != n:
            myStr = myStr + str[myIndex]
    return(myStr)
