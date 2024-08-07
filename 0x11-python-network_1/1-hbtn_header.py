#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id variable
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
