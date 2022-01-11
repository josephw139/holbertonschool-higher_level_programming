#!/usr/bin/python3
"""Task 1
"""


class Square:
    def __init__(self, size=0):
        """Square class with size checks

        Args:
            size (int): size of square. Defaults to 0.

        Raises:
            ValueError: size must be greater than 0
            TypeError: size must be an integer
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
