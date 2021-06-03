#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

with open("my_file_0.txt") as f:
    for line in f:
        print(line, end="")
