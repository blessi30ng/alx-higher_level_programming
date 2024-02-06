#!/usr/bin/python3

"""Contains class Student"""

class Student:
    """representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """dict representation of student instance"""
        return self.__dict__
