#!/usr/bin/pyhon3
"""Defines a base geometry class BaseGeometry"""

class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Area not  implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")
