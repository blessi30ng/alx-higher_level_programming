#!/usr/bin/python3
"""load, add, save"""

from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"

    try:
        json_list = load_from_json_file(filename)
    except FileNotFoundError:
        json_list = []

    for a in argv[1:]:
        json_list.append(a)

    save_to_json_file(json_list, filename)
