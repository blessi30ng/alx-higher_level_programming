#!/usr/bin/python3
""""defines a text file reading func"""

def read_file(filename=""):
    """print the contents  of a UTF8 text  file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
