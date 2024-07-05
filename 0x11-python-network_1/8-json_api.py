#!/usr/bin/python3
"""
 sends a POST request to http://0.0.0.0:5000/search_user
"""

from sys import argv
import requests


if __name__ == "__main__":
    let = "" if len(argv) == 1 else argv[1]
    payload = {"q": let}


    re = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = re.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
