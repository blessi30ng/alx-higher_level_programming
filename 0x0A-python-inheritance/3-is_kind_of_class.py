#!/usr/bin/python3
"""Defines a class and inherited class-checkin function"""

def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class"""

    if  isinstance(obj, a_class):
        return True
    return False
