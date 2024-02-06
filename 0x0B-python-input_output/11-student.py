#!/usr/bin/python3

"""Contains class Student"""

class Student:
    """representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """replaces all attributes of the Student instance"""
        if attrs is None:
            return self.__dict__
        new_d = {}
        for n in attrs:
            try:
                new_d[n] = self.__dict__[n]
            except FileNotFoundError:
                pass
        return new_d
