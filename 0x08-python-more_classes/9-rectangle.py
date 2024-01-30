#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns area of rectangle given width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns perimeter of rectangle given width and height
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of rectangle

        Represents the rect with # char
        """
        string = ""
        if self.__width != 0 or self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                    for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of a rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance that is a square with w==h==s"""
        return cls(size, size)
    
