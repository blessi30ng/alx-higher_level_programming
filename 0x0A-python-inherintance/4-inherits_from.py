#!/usr/bin/python3
""""Defines an inherited class_checking function"""

def inherits_from(obj, a_class):
    """Defines an inherited class-checking function"""

    if issubclass(type(obj), a_class) and type (obj) != a_class:
        return True
    return False
