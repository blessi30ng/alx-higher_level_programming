#!/usr/bin/python3
"""Defines a class-checking function"""

def is_same_class(obj, a_class):
    """check if an object is exactly an insatnce of a given class"""
    if type(obj) == a_class:
        return True
    return False
