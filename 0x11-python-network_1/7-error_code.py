#!/usr/bin/python3
'''
Python script that fetches
https://intranet.hbtn.io/status
'''


import requests
import sys


if __name__ == "__main__":

    res = int(requests.get(sys.argv[1]))

    if res >= 400:
        print("Error code: {}".format(res))
