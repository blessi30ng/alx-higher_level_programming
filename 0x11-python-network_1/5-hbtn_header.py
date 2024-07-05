#!/usr/bin/python3
"""
displays the value of the variable X-Request-Id in the response header
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-ID"))
