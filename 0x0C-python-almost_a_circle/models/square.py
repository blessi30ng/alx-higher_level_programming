#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """representation of a new square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """update square"""
        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for q, r in kwargs.items():
                if q == "id":
                    if r is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = r
                elif q == "size":
                    self.size = r
                elif q == "x":
                    self.x = r
                elif q == "y":
                    self.y = r


