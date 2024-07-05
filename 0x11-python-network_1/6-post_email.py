#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    value = value = {"email": argv[2]}

    re = requests.post(url, data=value)
    print(re.text)
