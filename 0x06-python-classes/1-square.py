#!/usr/bin/python3
"""Square class definition"""



class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __innit__(self, size=0):
        """Initializes a square

        Args:

            size(int):size of a side of the square
        Returns: None
        """

        self.__size = size
