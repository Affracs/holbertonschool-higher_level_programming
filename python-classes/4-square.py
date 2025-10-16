#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialise square with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size ** 2
