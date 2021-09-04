#!/usr/bin/python3
'''
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8)
'''


if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    import sys

    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    data = urllib.parse.urlencode(email).encode('utf8')
    req = urllib.request.Request(url, email)

    with urllib.request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)
