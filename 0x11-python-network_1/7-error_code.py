#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    re = requests.get(url)
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
