#!/usr/bin/python3
'''
Python script that fetches
https://intranet.hbtn.io/status
'''


import requests
import sys


if __name__ == "__main__":

    res = requests.get(sys.argv[1])
    code = res.status_code

    if code >= 400:
        print("Error code: {}".format(code))
        return

    print(res.text)
