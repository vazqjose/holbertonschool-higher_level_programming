#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

absnumber = abs(number)
lastdigit = absnumber % 10

if number < 0:
    lastdigit = lastdigit * -1

string = " "
msg = "Last digit of {} is {} and is {}"

if lastdigit > 5:
    string = 'greater than 5'
elif lastdigit == 0:
    string = '0'
elif lastdigit < 6 and lastdigit != 0:
    string = 'less than 6 and not 0'

print(msg.format(number, lastdigit, string))
