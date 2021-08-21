#!/usr/bin/python3
'''
Write a Python script that fetches an https address
    - You must use a with statement
    - You must only use the package urllib
    - You must use a with statement
    - Output should be (tabulation before each - ):
        Body response:$
            - type: <class 'bytes'>
            - content: b'OK'
            - utf8 content: OK
'''


if __name__ == "__main__":

    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
