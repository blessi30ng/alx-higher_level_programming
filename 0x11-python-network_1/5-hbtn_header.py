#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-Id"))
