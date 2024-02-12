#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """set x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """set y of rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` char"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for n in range(self.y)]
        for b in range(self.height):
            [print(" ", end="") for l in range(self.x)]
            [print("#", end="") for m in range(self.width)]
            print("")

    def __str__(self):
        """ Str format """
        str_pr = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        str_pr = str_pr.format(self.id, self.x, self.y, self.width, self.height)
        return str_pr

    def update(self, *args):
        """Update the Rectangle"""
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1

        elif kwargs and len(kwargs) != 0:
            for l, m in kwargs.items():
                if l == "id":
                    if m is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = m
                elif l == "width":
                    self.width = m
                elif l == "height":
                    self.height = m
                elif l == "x":
                    self.x = m
                elif l == "y":
                    self.y = m

