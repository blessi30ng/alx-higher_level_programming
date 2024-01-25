#!/usr/bin/python3
"""Defines a class Square"""


class Square:
 """Represents a square
    Attributes:
        size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """calculates the area of the square
        Returns:
            The area of the square
        """

        return self.__size * self.__size

    @property
    def size(self):
         """getter of size
        Returns:
            The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter of size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints square
        Returns:
            None
        """

        if self.__size == 0:
            print()
            return
        for l in range(self.__size):
            print("".join(["#" for m in range(self.__size)]))
