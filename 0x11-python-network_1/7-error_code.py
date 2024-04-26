#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

import sys
import requests


if __name__ == "_-main__":
    url = sys.argv[1]

    re = request.get(url)
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
