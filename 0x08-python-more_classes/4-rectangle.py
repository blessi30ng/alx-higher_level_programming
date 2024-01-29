#/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""

        self.width = width
        self.height = height

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
            string += "\n".join("#" * self.__width
                    for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of a rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
